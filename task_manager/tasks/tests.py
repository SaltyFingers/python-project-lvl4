# from django.test import TestCase
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
# from task_manager.tasks.models import Task
# from task_manager.users.models import User
# from task_manager.statuses.models import Status
# from task_manager.labels.models import Label
# from task_manager.tasks.forms import FilterTask

# # Create your tests here.
# OK_CODE = 200


# class TestTasks(TestCase):

#     fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

#     def setUp(self):
#         self.status1 = Status.objects.get(pk=1)
#         self.status2 = Status.objects.get(pk=2)
#         self.status3 = Status.objects.get(pk=3)
#         self.status4 = Status.objects.get(pk=4)

#         self.user1 = User.objects.get(pk=1)
#         self.user2 = User.objects.get(pk=2)
#         self.user3 = User.objects.get(pk=3)

#         self.task1 = Task.objects.get(pk=1)
#         self.task2 = Task.objects.get(pk=2)
#         self.task3 = Task.objects.get(pk=3)

#         self.label1 = Label.objects.get(pk=1)
#         self.label2 = Label.objects.get(pk=2)
#         self.label3 = Label.objects.get(pk=3)
#         self.label4 = Label.objects.get(pk=5)

#     def test_tasks_list(self):
#         self.client.force_login(self.user1)

#         response = self.client.get(reverse("tasks:list"))
#         tasks_list = list(response.context["tasks"])

#         test_task1, test_task2, test_task3 = tasks_list

#         self.assertTrue(response.status_code == OK_CODE)
#         self.assertTrue(test_task1.id == self.task1.id)
#         self.assertTrue(test_task1.name == self.task1.name)
#         self.assertTrue(test_task1.author.username == self.task1.author.username)  # noqa
#         self.assertTrue(test_task1.executor.username == self.task1.executor.username)  # noqa

#         self.assertTrue(test_task2.id == self.task2.id)
#         self.assertTrue(test_task2.name == self.task2.name)
#         self.assertTrue(test_task2.author.username == self.task2.author.username)  # noqa
#         self.assertTrue(test_task2.executor.username == self.task2.executor.username)  # noqa

#         self.assertTrue(test_task3.id == self.task3.id)
#         self.assertTrue(test_task3.name == self.task3.name)
#         self.assertTrue(test_task3.author.username == self.task3.author.username)  # noqa
#         self.assertTrue(test_task3.executor.username == self.task3.executor.username)  # noqa

#     def test_create_task(self):
#         self.client.force_login(self.user1)

#         new_task = {
#             "name": "TaskTask",
#             "description": "some description",
#             "status": self.status1.name,
#             "labels": [self.label1, self.label3],
#             "executor": self.user2.username,
#         }

#         response = self.client.post(reverse("tasks:create"),
#                                     new_task, follow=True)

#         created_task = Task.objects.last()

#         # self.assertRedirects(response, "/tasks/", status_code=302, target_status_code=200, fetch_redirect_response=True)
#         self.assertTrue(response.status_code == OK_CODE)
#         # self.assertContains(response, _("Task created successfully!"))
#         self.assertTrue(created_task.id == 4)
#         self.assertTrue(created_task.autor == self.user1.name)

#     def test_update_task(self):
#         self.client.force_login(self.user3)
#         task = self.task1

#         updated_data = {
#             "name": "Not easy task",
#             "executor": self.user1.username,
#         }

#         old_name = task.name
#         old_executor = task.executor

#         response = self.client.post(
#             reverse("tasks:update", args=(task.id,)),
#             updated_data,
#             follow=True
#         )

#         updated_task = Task.objects.get(id=task.id)

#         # self.assertRedirects(response, "/tasks/")
#         self.assertTrue(response.status_code == OK_CODE)
#         # self.assertContains(response, _("Task updated successfully!"))
#         self.assertFalse(updated_task.name == old_name)
#         self.assertFalse(updated_task.executor == old_executor)
#         self.assertTrue(updated_task.name == "Not easy task")

#     def test_delete_task_by_another_user(self):
#         self.client.force_login(self.user1)

#         response = self.client.post(
#             reverse("tasks:delete", args=(self.task1.id,)), follow=True
#         )

#         self.assertRedirects(response, "/tasks/")
#         self.assertTrue(Task.objects.filter(id=self.task1.id).exists())
#         self.assertContains(response,
#                             _("Task can only be deleted by it's author!"))

#     def test_delete_task(self):
#         self.client.force_login(self.user3)

#         response = self.client.post(
#             reverse("tasks:delete", args=(self.task1.id,)), follow=True
#         )

#         with self.assertRaises(Task.DoesNotExist):
#             Task.objects.get(id=self.task1.id)

#         # self.assertRedirects(response, "/tasks/")
#         self.assertTrue(response.status_code == OK_CODE)
#         self.assertContains(response, _("Task deleted successfully!"))

#     def test_filter_task_by_executor(self):
#         self.client.force_login(self.user1)

#         qs = Task.objects.all()
#         f = FilterTask(data={"executor": self.user1.id}, queryset=qs)
#         self.assertTrue(self.task1 in f.qs)
#         self.assertFalse(self.task3 in f.qs)

#     def test_filter_task_by_status(self):
#         self.client.force_login(self.user1)

#         qs = Task.objects.all()
#         f = FilterTask(data={"status": self.status4.id}, queryset=qs)
#         self.assertTrue(self.task3 in f.qs)
#         self.assertFalse(self.task1 in f.qs)

#     def test_filter_task_by_label(self):
#         self.client.force_login(self.user1)

#         qs = Task.objects.all()
#         f = FilterTask(data={"labels": self.label4.id}, queryset=qs)
#         self.assertTrue(self.task1 in f.qs and self.task2 in f.qs)
#         # self.assertTrue(self.task3 not in f.qs)
