# Generated by Django 4.2.5 on 2023-10-02 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user_time',
            field=models.CharField(max_length=50, verbose_name='Time'),
        ),
    ]