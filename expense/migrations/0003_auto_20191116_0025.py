# Generated by Django 2.2.7 on 2019-11-16 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20191115_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='expense_type',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
