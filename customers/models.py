from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError('Email is required to create User.')
        user = self.model(email=self.normalize_email(email), **other_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Adres email/login',
        max_length=255,
        unique=True
    )

    first_name = models.CharField(
        verbose_name='Imię',
        max_length=255
    )

    last_name = models.CharField(
        verbose_name='Nazwisko',
        max_length=255
    )

    phone = models.CharField(
        verbose_name='Telefon',
        blank=True,
        null=True,
        default='',
        max_length=200
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'