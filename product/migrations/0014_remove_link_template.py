# Generated by Django 2.1.7 on 2019-02-24 19:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0013_link_template'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='template',
        ),
    ]
