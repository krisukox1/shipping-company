# Generated by Django 2.1.3 on 2018-11-29 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181129_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='Imie',
        ),
    ]
