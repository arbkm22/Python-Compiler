# Generated by Django 2.1 on 2020-09-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200927_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='images',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
