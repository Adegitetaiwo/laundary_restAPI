# Generated by Django 3.1.2 on 2020-10-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_logics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickupclass',
            name='address',
            field=models.CharField(blank=True, default='Nan', max_length=500, null=True),
        ),
    ]