# Generated by Django 3.2.9 on 2021-12-02 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20211202_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.CharField(default=0.0, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='deposit',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
