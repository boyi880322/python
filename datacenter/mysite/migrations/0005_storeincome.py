# Generated by Django 3.1.2 on 2020-12-01 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20201201_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_year', models.CharField(max_length=4)),
                ('income_month', models.CharField(max_length=2)),
                ('income', models.PositiveIntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.branch')),
            ],
        ),
    ]