# Generated by Django 3.1 on 2021-03-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AddField(
            model_name='product',
            name='user_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
