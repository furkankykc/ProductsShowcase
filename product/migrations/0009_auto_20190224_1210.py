# Generated by Django 2.1.7 on 2019-02-24 12:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0008_auto_20190224_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seo',
            old_name='tag',
            new_name='name',
        ),
    ]
