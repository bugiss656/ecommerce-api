# Generated by Django 4.1.3 on 2024-02-26 14:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productparameter_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productparameter',
            name='value',
        ),
        migrations.CreateModel(
            name='ProductParameterValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.CharField(default='', max_length=200, verbose_name='Opis parametru')),
                ('product_parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter_values', to='products.productparameter')),
            ],
        ),
    ]