# Generated by Django 3.2.8 on 2021-10-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_user_barista'),
    ]

    operations = [
        migrations.AddField(
            model_name='barista',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='barista',
            name='profile_pic',
            field=models.ImageField(default='pp-default.png', upload_to=''),
        ),
    ]