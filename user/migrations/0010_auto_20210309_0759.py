# Generated by Django 3.1.5 on 2021-03-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20210308_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='attribute_values',
            field=models.JSONField(max_length=500, verbose_name='Item Details JSON'),
        ),
    ]
