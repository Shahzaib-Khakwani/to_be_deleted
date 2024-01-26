# Generated by Django 4.2.7 on 2023-12-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_order_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="productrating",
            name="downloads",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="productrating",
            name="file",
            field=models.FileField(null=True, upload_to="product_files/"),
        ),
    ]
