# Generated by Django 4.0.2 on 2022-06-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0004_rename_label_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True, related_name="tasks", to="labels.Label"
            ),
        ),
    ]
