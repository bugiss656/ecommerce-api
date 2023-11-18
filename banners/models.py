from django.db import models


class Banner(models.Model):
    title = models.CharField(
        'Tytuł banera',
        blank=True,
        null=True,
        default='',
        max_length=100
    )
    is_active = models.BooleanField(
        'Baner aktywny?',
        default=True
    )
    ordering_number = models.IntegerField(
        'Numer porządkowy banera',
        blank=True,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Baner (zdjęcie)',
        blank=True,
        null=True,
        default='',
        upload_to='images'
    )
    href = models.URLField(
        'Link do podstrony',
        blank=True,
        null=True,
        default=''
    )

    class Meta:
        ordering = ['ordering_number']

    def __str__(self):
        return self.title