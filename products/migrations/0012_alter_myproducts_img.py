# Generated by Django 3.2 on 2022-02-07 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_myproducts_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproducts',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
