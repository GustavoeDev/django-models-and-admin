# Generated by Django 5.1.4 on 2024-12-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_category_products_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
    ]