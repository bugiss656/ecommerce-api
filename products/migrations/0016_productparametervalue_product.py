# Generated by Django 4.1.3 on 2024-02-26 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_remove_productparameter_value_productparametervalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='productparametervalue',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
