# Generated by Django 3.2.6 on 2021-08-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
