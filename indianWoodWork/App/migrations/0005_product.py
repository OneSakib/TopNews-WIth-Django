# Generated by Django 4.0.1 on 2022-01-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_imageslide_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=350)),
                ('smallimage', models.ImageField(default='', upload_to='')),
                ('hdimage1', models.ImageField(default='', upload_to='')),
                ('hdimage2', models.ImageField(default='', upload_to='')),
                ('hdimage3', models.ImageField(default='', upload_to='')),
                ('hdimage4', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
