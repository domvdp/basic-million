# Generated by Django 3.1.5 on 2021-10-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211019_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]