# Generated by Django 3.0.1 on 2020-01-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('volume', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=100)),
                ('is_in_home', models.IntegerField(max_length=100)),
                ('category', models.IntegerField(max_length=100)),
            ],
        ),
    ]
