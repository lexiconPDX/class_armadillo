# Generated by Django 3.0.6 on 2020-06-03 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200602_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='age',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='is_cell',
        ),
    ]