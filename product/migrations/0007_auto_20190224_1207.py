# Generated by Django 2.1.7 on 2019-02-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0006_auto_20190224_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='tag',
            field=models.CharField(max_length=30),
        ),
    ]
