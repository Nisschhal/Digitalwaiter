# Generated by Django 3.2.5 on 2022-02-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0005_order_is_delivered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_delivered',
            field=models.BooleanField(default=False),
        ),
    ]
