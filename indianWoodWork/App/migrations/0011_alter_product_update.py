# Generated by Django 4.0.1 on 2022-02-01 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_product_product_cat_product_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='update',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
