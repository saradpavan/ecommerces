# Generated by Django 4.1.6 on 2023-03-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default=2, upload_to='images'),
            preserve_default=False,
        ),
    ]
