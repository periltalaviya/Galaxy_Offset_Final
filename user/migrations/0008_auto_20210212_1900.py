# Generated by Django 3.1.5 on 2021-02-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aqutouscoating',
            name='aqutous_coating_type',
            field=models.CharField(max_length=35, verbose_name='Aqutous Coating Type'),
        ),
    ]
