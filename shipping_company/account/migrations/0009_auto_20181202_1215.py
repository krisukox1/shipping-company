# Generated by Django 2.1.3 on 2018-12-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20181129_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='PESEL',
            field=models.IntegerField(blank=True),
        ),
    ]
