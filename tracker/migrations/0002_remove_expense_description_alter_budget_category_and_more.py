# Generated by Django 4.2.13 on 2024-07-01 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='description',
        ),
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]