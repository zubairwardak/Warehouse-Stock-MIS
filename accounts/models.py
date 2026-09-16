from django.db import models
from django.contrib.auth.models import AbstractUser



# ==========================
# Permission Model
# ==========================

class Permission(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name




# ==========================
# Department Model
# ==========================

class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.name





# ==========================
# Role Model
# ==========================

class Role(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )


    permissions = models.ManyToManyField(
        Permission,
        blank=True
    )


    def __str__(self):
        return self.name





# ==========================
# Custom User Model
# ==========================

class User(AbstractUser):

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


    status = models.BooleanField(
        default=True
    )


    def __str__(self):
        return self.username