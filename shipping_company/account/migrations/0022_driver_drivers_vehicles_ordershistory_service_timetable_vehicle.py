# Generated by Django 2.1.3 on 2018-12-08 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20181203_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('ID_kierowcy', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers_Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_kierowcy', models.ManyToManyField(to='account.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersHistory',
            fields=[
                ('ID_zamowienia', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('ID_uslugi', models.AutoField(primary_key=True, serialize=False)),
                ('opis_uslugi', models.CharField(max_length=100)),
                ('koszt', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('ID_terminu', models.AutoField(primary_key=True, serialize=False)),
                ('data_pocz', models.DateField()),
                ('data_kon', models.DateField()),
                ('ID_kierowcy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Driver')),
                ('ID_zamowienia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('Nr_rej', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('marka', models.CharField(blank=True, max_length=40, null=True)),
                ('model', models.CharField(blank=True, max_length=40, null=True)),
                ('atrybut', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]