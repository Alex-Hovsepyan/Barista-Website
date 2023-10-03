# Generated by Django 4.2.5 on 2023-10-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=80, verbose_name='Address')),
                ('social1', models.URLField(verbose_name='Social 1')),
                ('social2', models.URLField(verbose_name='Social 2')),
                ('social3', models.URLField(verbose_name='Social 3')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Footer',
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='OpenHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30, verbose_name='Day')),
                ('time', models.CharField(max_length=20, verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Open Hours',
                'verbose_name_plural': 'Open Hours',
            },
        ),
    ]
