import uuid
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


# class Address(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#         editable=False
#     )
    
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     street = models.CharField(
#         verbose_name='Ulica zamieszkania',
#         blank=True,
#         null=True,
#         default='',
#         max_length=200
#     )

#     building_number = models.CharField(
#         verbose_name='Numer domu/lokalu',
#         blank=True,
#         null=True,
#         default='',
#         max_length=200
#     )

#     city = models.CharField(
#         verbose_name='Miasto',
#         blank=True,
#         null=True,
#         default='',
#         max_length=200
#     )

#     zip_code = models.CharField(
#         verbose_name='Kod pocztowy',
#         blank=True,
#         null=True,
#         default='',
#         max_length=200
#     )

#     def __str__(self):
#         return f'{self.street} {self.building_number} - {self.user.email}'