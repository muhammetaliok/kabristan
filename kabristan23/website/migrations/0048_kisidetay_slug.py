# Generated by Django 4.0.3 on 2022-07-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0047_alter_kisidetay_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisidetay',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
