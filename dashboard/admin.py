# dashboard/admin.py
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()  # Use the current user model

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'groups'),
        }),
    )

class CustomGroupAdmin(BaseGroupAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Unregister the default User and Group admin models
admin.site.unregister(User)
admin.site.unregister(Group)

# Register custom User and Group admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)
