# Generated by Django 3.2.9 on 2022-01-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20220122_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
