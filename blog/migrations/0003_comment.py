# Generated by Django 3.1 on 2021-03-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_recommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
