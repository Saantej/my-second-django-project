# Generated by Django 4.1.4 on 2023-01-08 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productcategory",
            options={"verbose_name_plural": "Product Categories"},
        ),
    ]
