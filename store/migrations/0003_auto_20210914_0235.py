# Generated by Django 3.2.6 on 2021-09-14 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_users_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minsysreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('os', models.TextField(blank=True, null=True)),
                ('memory', models.TextField(blank=True, null=True)),
                ('graphics', models.TextField(blank=True, null=True)),
                ('directX', models.TextField(blank=True, null=True)),
                ('storage', models.TextField(blank=True, null=True)),
                ('additional', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recsysreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('os', models.TextField(blank=True, null=True)),
                ('memory', models.TextField(blank=True, null=True)),
                ('graphics', models.TextField(blank=True, null=True)),
                ('directX', models.TextField(blank=True, null=True)),
                ('storage', models.TextField(blank=True, null=True)),
                ('additional', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='franchise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='franchise', to='store.franchise'),
        ),
        migrations.CreateModel(
            name='sysreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Recsysreq', to='store.recsysreq')),
                ('min', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Minsysreq', to='store.minsysreq')),
            ],
        ),
    ]
