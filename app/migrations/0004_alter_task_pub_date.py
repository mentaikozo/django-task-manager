# Generated by Django 5.1.4 on 2025-01-03 02:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日'),
        ),
    ]
