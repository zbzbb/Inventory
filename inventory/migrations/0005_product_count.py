# Generated by Django 5.0 on 2023-12-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_invention_product_code_invention_supplier_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
