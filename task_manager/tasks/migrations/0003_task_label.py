# Generated by Django 4.0.2 on 2022-06-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0002_alter_task_author_alter_task_executor"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="label",
            field=models.ManyToManyField(
                null=True, related_name="tasks", to="labels.Label"
            ),
        ),
    ]
