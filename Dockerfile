FROM python:3.12-alpine AS builder

RUN apk add --no-cache libgcc mariadb-connector-c pkgconf mariadb-dev postgresql-dev linux-headers

WORKDIR /opt/connect_store
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/connect_store/
COPY manage.py /opt/connect_store/
COPY django_connect_store /opt/connect_store/django_connect_store/
COPY django_connect_backend /opt/connect_store/django_connect_backend/

FROM builder AS install
WORKDIR /opt/connect_store
ENV VIRTUAL_ENV=/opt/connect_store/venv

RUN python -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r /opt/connect_store/requirements.txt

FROM install as run

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "--noreload", "0.0.0.0:8000"]
