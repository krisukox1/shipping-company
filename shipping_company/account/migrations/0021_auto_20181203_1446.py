# Generated by Django 2.1.3 on 2018-12-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20181203_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='kod_pocztowy',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='nr_budynku',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='nr_lokalu',
            field=models.IntegerField(null=True),
        ),
    ]
