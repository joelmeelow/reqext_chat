# Generated by Django 5.1.2 on 2024-10-20 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0011_order_user_alter_bonus_date_gained_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='date_gained',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 16, 49, 46, 826264, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='date_entered',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 16, 49, 46, 820264, tzinfo=datetime.timezone.utc), verbose_name='date item entered'),
        ),
        migrations.AlterField(
            model_name='mostsearched',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 16, 49, 46, 826264, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 16, 49, 46, 855266, tzinfo=datetime.timezone.utc), verbose_name='order date'),
        ),
        migrations.AlterField(
            model_name='productratingreview',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2024, 10, 20, 16, 49, 46, 825267, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
