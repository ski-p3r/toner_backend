# Generated by Django 4.2.5 on 2023-09-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='sample', max_length=12),
            preserve_default=False,
        ),
    ]