# Generated by Django 2.0.2 on 2018-02-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cust_data', '0004_auto_20180213_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
