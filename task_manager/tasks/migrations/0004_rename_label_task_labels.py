# Generated by Django 4.0.2 on 2022-06-28 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='label',
            new_name='labels',
        ),
    ]
