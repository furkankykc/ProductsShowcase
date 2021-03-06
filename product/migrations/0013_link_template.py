# Generated by Django 2.1.7 on 2019-02-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0012_auto_20190224_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='template',
            field=models.CharField(
                choices=[('navbar.html', 'navbar.html'), ('link.html', 'link.html'), ('index.html', 'index.html'),
                         ('default.html', 'default.html'), ('product.html', 'product.html'),
                         ('nav-item.html', 'nav-item.html'), ('nav-dropdown.html', 'nav-dropdown.html'),
                         ('about.html', 'about.html'), ('base.html', 'base.html'), ('contact.html', 'contact.html'),
                         ('pricing.html', 'pricing.html'), ('navs', 'navs'), ('work.html', 'work.html'),
                         ('dynamic.html', 'dynamic.html'), ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                         ('content.html', 'content.html')], default='default.html', max_length=20),
        ),
    ]
