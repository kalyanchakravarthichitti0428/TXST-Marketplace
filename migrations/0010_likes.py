# Generated by Django 3.1.3 on 2023-03-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_chat_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
