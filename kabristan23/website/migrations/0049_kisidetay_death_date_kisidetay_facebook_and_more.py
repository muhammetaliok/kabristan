# Generated by Django 4.0.3 on 2022-07-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0048_kisidetay_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisidetay',
            name='death_date',
            field=models.DateField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='kisidetay',
            name='facebook',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kisidetay',
            name='instagram',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='kisidetay',
            name='twitter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
