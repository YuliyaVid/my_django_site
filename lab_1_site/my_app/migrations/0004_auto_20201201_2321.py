# Generated by Django 3.1.3 on 2020-12-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20201201_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Passport_number',
            field=models.IntegerField(null=True),
        ),
    ]
