# Generated by Django 4.2.5 on 2023-10-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_menucontent_new_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='images', verbose_name='Background')),
                ('img', models.ImageField(upload_to='images', verbose_name='Image')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('info', models.CharField(max_length=40, verbose_name='Info')),
                ('text', models.TextField(verbose_name='Text')),
                ('rating', models.FloatField(verbose_name='Rating')),
            ],
        ),
    ]
