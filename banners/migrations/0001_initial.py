# Generated by Django 4.1.3 on 2023-11-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Tytuł banera')),
                ('is_active', models.BooleanField(default=True, verbose_name='Baner aktywny?')),
                ('ordering_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numer porządkowy banera')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images', verbose_name='Baner (zdjęcie)')),
                ('href', models.URLField(blank=True, default='', null=True, verbose_name='Link do podstrony')),
            ],
            options={
                'ordering': ['ordering_number'],
            },
        ),
    ]
