# Generated by Django 2.0.2 on 2018-02-13 03:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cust_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='DOB',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
