# Generated by Django 3.1.2 on 2020-10-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_logics', '0005_remove_testimonialclass_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialclass',
            name='passport',
            field=models.ImageField(default=False, upload_to='image'),
            preserve_default=False,
        ),
    ]
