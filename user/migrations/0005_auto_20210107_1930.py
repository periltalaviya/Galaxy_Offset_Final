# Generated by Django 3.1.2 on 2021-01-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210107_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_Price',
            field=models.IntegerField(default=0.0, verbose_name='Product Price/Piece'),
        ),
    ]
