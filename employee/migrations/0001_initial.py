# Generated by Django 3.2.4 on 2021-09-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(unique=True)),
                ('empname', models.CharField(max_length=100)),
                ('empemail', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=15)),
                ('empaddress', models.CharField(max_length=200)),
            ],
        ),
    ]
