# Generated by Django 3.2.6 on 2021-09-14 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_system_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
