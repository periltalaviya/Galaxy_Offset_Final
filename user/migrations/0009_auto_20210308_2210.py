# Generated by Django 3.1.5 on 2021-03-08 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20210308_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='attribute_values',
            field=models.CharField(max_length=500, verbose_name='Item Details JSON'),
        ),
    ]