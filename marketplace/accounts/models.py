from django.contrib.auth.models import AbstractUser
from django.db import models

# Business Model

class Business(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Role Model

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Permissions
    can_create_product = models.BooleanField(default=False)
    can_edit_product = models.BooleanField(default=False)
    can_approve_product = models.BooleanField(default=False)
    can_delete_product = models.BooleanField(default=False)
    can_manage_users = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Custom User Model

class User(AbstractUser):
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, null=True, blank=True
    )
    role = models.ForeignKey(
        Role, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.username

