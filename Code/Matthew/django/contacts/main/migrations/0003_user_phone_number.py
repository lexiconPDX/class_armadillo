# Generated by Django 3.0.6 on 2020-06-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200629_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
