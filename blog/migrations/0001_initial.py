# Generated by Django 3.1 on 2021-03-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='blogpics')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
