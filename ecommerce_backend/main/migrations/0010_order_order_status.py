# Generated by Django 4.2.7 on 2023-12-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_orderitem_price_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_status",
            field=models.BooleanField(default=False),
        ),
    ]
