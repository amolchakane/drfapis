# Generated by Django 4.0.3 on 2022-04-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
    ]
