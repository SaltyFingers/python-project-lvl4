# Generated by Django 4.1 on 2022-08-16 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tasks", "0006_alter_task_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="executor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="works_on",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
