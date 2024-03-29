# Generated by Django 4.1.3 on 2024-02-25 15:58

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(blank=True, default='', max_length=10000, null=True, verbose_name='Opis produktu'),
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200, verbose_name='Parametr produktu')),
                ('value_string', models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Opis parametru (tekst)')),
                ('value_number', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5, null=True, verbose_name='Opis parametru (liczba)')),
                ('value_boolean', models.BooleanField(blank=True, default='', null=True, verbose_name='Opis parametru (wartość logiczna)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='products.category')),
            ],
        ),
    ]
