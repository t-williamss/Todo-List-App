# Generated by Django 2.1.7 on 2019-05-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20190520_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.CharField(default='Uncomplete', max_length=25),
        ),
    ]
