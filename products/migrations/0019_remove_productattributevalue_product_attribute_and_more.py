# Generated by Django 4.1.3 on 2024-02-29 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_create_productattribute_productattributevalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattributevalue',
            name='product_attribute',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
        migrations.DeleteModel(
            name='ProductAttributeValue',
        ),
    ]