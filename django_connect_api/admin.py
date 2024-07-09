from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token


class CustomTokenAdmin(TokenAdmin):
    list_display = ("key", "user", "created")
    fields = ("user",)
    ordering = ("-created",)


admin.site.register(Token, CustomTokenAdmin)
admin.site.unregister(Token)


def create_auth_token(modeladmin, request, queryset):
    for user in queryset:
        Token.objects.get_or_create(user=user)


create_auth_token.short_description = "Create auth token for selected users"


class CustomUserAdmin(UserAdmin):
    actions = [create_auth_token]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
