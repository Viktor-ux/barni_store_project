# Generated by Django 4.1.4 on 2023-01-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='image'),
        ),
    ]
