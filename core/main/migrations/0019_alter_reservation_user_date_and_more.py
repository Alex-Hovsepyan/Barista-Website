# Generated by Django 4.2.5 on 2023-10-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_reservation_user_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user_date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_time',
            field=models.TimeField(verbose_name='Time'),
        ),
    ]