# Generated by Django 2.1.7 on 2019-02-24 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.CharField(choices=[('navbar.html', 'navbar.html'), ('index.html', 'index.html'),
                                                       ('default.html', 'default.html'),
                                                       ('product.html', 'product.html'),
                                                       ('nav-item.html', 'nav-item.html'),
                                                       ('nav-dropdown.html', 'nav-dropdown.html'),
                                                       ('about.html', 'about.html'), ('base.html', 'base.html'),
                                                       ('contact.html', 'contact.html'),
                                                       ('pricing.html', 'pricing.html'), ('navs', 'navs'),
                                                       ('work.html', 'work.html'), ('dynamic.html', 'dynamic.html'),
                                                       ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                                                       ('content.html', 'content.html')], default='default.html',
                                              max_length=20)),
                ('name', models.CharField(max_length=15)),
                ('model', models.CharField(max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('skype', models.CharField(max_length=15)),
                ('facebook', models.CharField(max_length=15)),
                ('instagram', models.CharField(max_length=15)),
                ('website', models.CharField(max_length=15)),
                ('about', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DropDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('url', models.CharField(default='/', max_length=20)),
                ('items', models.ManyToManyField(blank=True, related_name='_dropdown_items_+', to='product.DropDown')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('template', models.CharField(choices=[('navbar.html', 'navbar.html'), ('index.html', 'index.html'),
                                                       ('default.html', 'default.html'),
                                                       ('product.html', 'product.html'),
                                                       ('nav-item.html', 'nav-item.html'),
                                                       ('nav-dropdown.html', 'nav-dropdown.html'),
                                                       ('about.html', 'about.html'), ('base.html', 'base.html'),
                                                       ('contact.html', 'contact.html'),
                                                       ('pricing.html', 'pricing.html'), ('navs', 'navs'),
                                                       ('work.html', 'work.html'), ('dynamic.html', 'dynamic.html'),
                                                       ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                                                       ('content.html', 'content.html')], default='default.html',
                                              max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(default='default', max_length=20)),
                ('template', models.CharField(choices=[('navbar.html', 'navbar.html'), ('index.html', 'index.html'),
                                                       ('default.html', 'default.html'),
                                                       ('product.html', 'product.html'),
                                                       ('nav-item.html', 'nav-item.html'),
                                                       ('nav-dropdown.html', 'nav-dropdown.html'),
                                                       ('about.html', 'about.html'), ('base.html', 'base.html'),
                                                       ('contact.html', 'contact.html'),
                                                       ('pricing.html', 'pricing.html'), ('navs', 'navs'),
                                                       ('work.html', 'work.html'), ('dynamic.html', 'dynamic.html'),
                                                       ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                                                       ('content.html', 'content.html')], default='default.html',
                                              max_length=20)),
                ('dropdown', models.ManyToManyField(null=True, to='product.DropDown')),
            ],
        ),
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('url', models.CharField(default='/', max_length=20)),
                ('desc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=15)),
                ('title', models.CharField(default='', max_length=70)),
                ('locale', models.CharField(default='', max_length=10)),
                ('description', models.CharField(default='', max_length=170)),
                ('template', models.CharField(choices=[('navbar.html', 'navbar.html'), ('index.html', 'index.html'),
                                                       ('default.html', 'default.html'),
                                                       ('product.html', 'product.html'),
                                                       ('nav-item.html', 'nav-item.html'),
                                                       ('nav-dropdown.html', 'nav-dropdown.html'),
                                                       ('about.html', 'about.html'), ('base.html', 'base.html'),
                                                       ('contact.html', 'contact.html'),
                                                       ('pricing.html', 'pricing.html'), ('navs', 'navs'),
                                                       ('work.html', 'work.html'), ('dynamic.html', 'dynamic.html'),
                                                       ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                                                       ('content.html', 'content.html')], default='default.html',
                                              max_length=20)),
                ('components', models.ManyToManyField(to='product.Components')),
                ('footer',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Footer')),
                ('navbar',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Navbar')),
            ],
        ),
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('time', models.CharField(max_length=15)),
                ('color', models.CharField(
                    choices=[('green', 'Green'), ('red', 'Red'), ('yel', 'Yellow'), ('blue', 'Blue'),
                             ('white', 'White')], default='white', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('about', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SeoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('template', models.CharField(choices=[('navbar.html', 'navbar.html'), ('index.html', 'index.html'),
                                                       ('default.html', 'default.html'),
                                                       ('product.html', 'product.html'),
                                                       ('nav-item.html', 'nav-item.html'),
                                                       ('nav-dropdown.html', 'nav-dropdown.html'),
                                                       ('about.html', 'about.html'), ('base.html', 'base.html'),
                                                       ('contact.html', 'contact.html'),
                                                       ('pricing.html', 'pricing.html'), ('navs', 'navs'),
                                                       ('work.html', 'work.html'), ('dynamic.html', 'dynamic.html'),
                                                       ('footer.html', 'footer.html'), ('slide.html', 'slide.html'),
                                                       ('content.html', 'content.html')], default='default.html',
                                              max_length=20)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(default='/', max_length=200)),
                ('short_desc', models.CharField(max_length=50)),
                ('button_text', models.CharField(default='default', max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='slider',
            name='item',
            field=models.ManyToManyField(null=True, to='product.SliderItem'),
        ),
        migrations.AddField(
            model_name='page',
            name='slider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Slider'),
        ),
        migrations.AddField(
            model_name='navbar',
            name='item',
            field=models.ManyToManyField(null=True, to='product.NavItem'),
        ),
    ]
