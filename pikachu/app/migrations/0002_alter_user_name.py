# Generated by Django 3.2.8 on 2021-10-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
