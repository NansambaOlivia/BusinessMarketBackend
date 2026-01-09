from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Business, Role

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'business', 'role', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'business', 'role')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ()

    # Fields to display in the admin form
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'business', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'business', 'role', 'is_active', 'is_staff')}
        ),
    )

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'can_create_product', 'can_edit_product', 'can_approve_product', 'can_delete_product', 'can_manage_users')
    list_filter = ('can_create_product', 'can_edit_product', 'can_approve_product', 'can_delete_product', 'can_manage_users')
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Permissions', {
            'fields': ('can_create_product', 'can_edit_product', 'can_approve_product', 'can_delete_product', 'can_manage_users')
        }),
    )
