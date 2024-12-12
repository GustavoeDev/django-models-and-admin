# Generated by Django 5.1.4 on 2024-12-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_products_alter_product_createdat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products_category', to='products.category'),
        ),
    ]
