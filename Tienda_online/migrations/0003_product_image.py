# Generated by Django 4.2.5 on 2023-09-26 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda_online', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]