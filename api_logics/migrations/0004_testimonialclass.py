# Generated by Django 3.1.2 on 2020-10-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_logics', '0003_auto_20201024_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonialClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('passport', models.ImageField(upload_to='image')),
                ('testimony', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
