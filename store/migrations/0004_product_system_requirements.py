# Generated by Django 3.2.6 on 2021-09-14 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210914_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='system_requirements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.sysreq'),
        ),
    ]
