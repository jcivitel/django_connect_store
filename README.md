[![](https://img.shields.io/maintenance/yes/2024)](https://github.com/jcivitel/)
[![Static Badge](https://img.shields.io/badge/GitHub-jcivitell-green?logo=github)](https://github.com/jcivitel/django_connect_store)
[![GitHub Repo stars](https://img.shields.io/github/stars/jcivitel/django_connect_store)](https://github.com/jcivitel/django_connect_store)
[![Docker Pulls](https://img.shields.io/docker/pulls/jcivitell/connect_store?logo=docker)](https://hub.docker.com/r/jcivitell/connect_store)
[![Docker Stars](https://img.shields.io/docker/stars/jcivitell/connect_store?logo=docker)](https://hub.docker.com/r/jcivitell/connect_store)
[![Docker Image Size](https://img.shields.io/docker/image-size/jcivitell/connect_store/latest?logo=docker)](https://hub.docker.com/r/jcivitell/connect_store)


# Connection Manager

## Overview

This Django-based web application allows users to manage their SSH connections (and other protocols) and access them
quickly. It provides a user-friendly dashboard for managing connections and quick access to frequently used connections.

## Features

- User-specific dashboard
- Management of connections (SSH, FTP, SFTP, etc.)
- Quick access to recently used connections
- Direct launch of the corresponding application when clicking on a connection

## Technologies

- Python 3.x
- Django 3.x
- Bootstrap 5.x

## Installation

1. Clone the repository:

```
git clone https://github.com/jcivitel/django_connect_store.git
cd ssh-connection-manager
```

2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Run database migration:

```
python manage.py migrate
```

## Usage

1. Open a web browser and navigate to `http://localhost:8000`
2. Log in with your superuser credentials
3. Add new connections via the dashboard
4. Click on a connection to open the corresponding application

## Contributing

Contributions are welcome! Please create an issue or pull request for suggestions or improvements.

## License

[MIT License](https://opensource.org/licenses/MIT)

# Contributors
[![Contributors Display](https://badges.pufler.dev/contributors/jcivitel/django_connect_store?size=50&padding=5&bots=false)](https://github.com/jcivitel/django_connect_store/graphs/contributors)
