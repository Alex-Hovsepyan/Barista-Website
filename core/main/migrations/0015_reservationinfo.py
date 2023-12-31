# Generated by Django 4.2.5 on 2023-10-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(upload_to='images', verbose_name='Background')),
                ('button', models.CharField(max_length=30, verbose_name='Button')),
                ('img', models.ImageField(upload_to='images', verbose_name='Image')),
            ],
        ),
    ]
