# Generated by Django 4.1.3 on 2024-02-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_description_productparameter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productparameter',
            name='value_boolean',
        ),
        migrations.RemoveField(
            model_name='productparameter',
            name='value_number',
        ),
        migrations.RemoveField(
            model_name='productparameter',
            name='value_string',
        ),
        migrations.AddField(
            model_name='productparameter',
            name='value',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Opis parametru'),
        ),
        migrations.AlterField(
            model_name='productparameter',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Nazwa parametru produktu'),
        ),
    ]
