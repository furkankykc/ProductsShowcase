# Generated by Django 2.1.7 on 2019-02-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0004_auto_20190224_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
