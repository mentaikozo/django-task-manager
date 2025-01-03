# Generated by Django 5.1.4 on 2025-01-03 02:49

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'タスク', 'verbose_name_plural': 'タスク'},
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default=1, help_text='1~10で設定、10が最優先', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='優先度'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, verbose_name='タスク名'),
        ),
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='メモ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateField(default=datetime.date(2025, 1, 3), verbose_name='登録日'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, '済'), (0, '未')], default=0, verbose_name='ステータス'),
        ),
    ]