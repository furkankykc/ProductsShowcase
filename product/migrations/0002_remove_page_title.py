# Generated by Django 2.1.7 on 2019-02-24 11:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='title',
        ),
    ]