# Generated by Django 4.0.1 on 2022-01-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_imageslide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslide',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]