# Generated by Django 4.1.3 on 2024-02-29 14:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_productattributevalue_product_attribute_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200, verbose_name='Nazwa atrybutu produktu')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(default='', max_length=200, verbose_name='Opis parametru')),
                ('product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='products.productattribute')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(default='', to='products.productattributevalue'),
        ),
    ]
