# Generated by Django 4.2.5 on 2023-09-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered')], default='pending', max_length=10),
        ),
    ]