# Generated by Django 4.0.5 on 2022-06-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierservice',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
