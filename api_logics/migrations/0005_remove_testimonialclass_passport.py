# Generated by Django 3.1.2 on 2020-10-24 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_logics', '0004_testimonialclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialclass',
            name='passport',
        ),
    ]
