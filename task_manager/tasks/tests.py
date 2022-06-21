from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label

# Create your tests here.
OK_CODE = 200

class TestTasks(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

    def setUp(self):
        self.status = Status.objects.get(pk=1)

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)

    def test_tasks_list(self):
        self.client.force_login(self.user1)
        
        response = self.client.get(reverse("tasks:list"))
        tasks_list = list(response.context["tasks"])

        task1, task2, task3 = tasks_list

        self.assertTrue(response.status_code == OK_CODE)
        self.assertTrue(task1.id == 1)
        self.assertTrue(task1.name == "Easy task")
        self.assertTrue(task1.author.username == "Chicharito")
        self.assertTrue(task1.executor.username == "xXxJONNYxXx")

        self.assertTrue(task2.id == 2)
        self.assertTrue(task2.name == "Задача")
        self.assertTrue(task2.author.username == "IvanIvan")
        self.assertTrue(task2.executor.username == "Chicharito")

        self.assertTrue(task3.id == 3)
        self.assertTrue(task3.name == "Task to manage")
        self.assertTrue(task3.author.username == "xXxJONNYxXx")
        self.assertTrue(task3.executor.username == "IvanIvan")

    def test_create_task(self):
        self.client.force_login(self.user1)

        new_task = {
            "name": "TaskTask",
            "description": "some description lol",
            "status": self.status.name,
            "executor": self.user2.username,
        }

        response = self.client.post(reverse("tasks:create"), new_task, follow=True)

        created_task = Task.objects.last()

        self.assertTrue(response.status_code == OK_CODE)
        self.assertRedirects(response, "/tasks/")
        self.assertContains(response, _("Task created successfully!"))
        self.assertTrue(created_task.id == 4)
        self.assertTrue(created_task.autor == self.user1.name)

    def test_update_task(self):
        self.client.force_login(self.user3)
        task = self.task1
        
        updated_data = {
            "name": "Not easy task",
            "executor": self.user1.username,
        }

        old_name = task.name
        old_executor = task.executor

        response = self.client.post(
            reverse("tasks:update", args=(task.id,)), updated_data, follow=True
        )

        updated_task = Task.objects.get(id=task.id)

        self.assertRedirects(response, "/tasks/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Task updated successfully!"))
        self.assertFalse(updated_task.name == old_name)
        self.assertFalse(updated_task.executor == old_executor)
        self.assertTrue(updated_task.name == "Not easy task")

    def test_delete_task(self):
        self.client.force_login(self.user3)

        # with self.assertRaises(Exception):
        #     self.client.post(
        #         reverse("tasks:delete", args=(self.task1.id,)), follow=True
        #     )

        # Status.objects.all().delete()
        # Label.objects.all().delete()
        # User.objects.get(id=self.user2.id)


        response = self.client.post(
            reverse("tasks:delete", args=(self.task1.id,)), follow=True
        )

        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task1.id)

        self.assertRedirects(response, "/tasks/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Task deleted successfully!"))