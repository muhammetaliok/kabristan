# Generated by Django 4.0.3 on 2022-07-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_useraddpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='userPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldpassword', models.CharField(blank=True, max_length=200, null=True)),
                ('newpassword', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
