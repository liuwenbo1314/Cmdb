# Generated by Django 2.2.1 on 2019-12-31 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_tasksorder_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksorder',
            name='host',
        ),
    ]
