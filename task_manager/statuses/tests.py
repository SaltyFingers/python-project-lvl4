from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status

# Create your tests here.
OK_CODE = 200

class TestStatuses(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
        self.status4 = Status.objects.get(pk=4)

    def test_statuses_list(self):
        self.client.force_login(self.user1)

        response = self.client.get(reverse("statuses:list"))
        statuses_list = list(response.context["statuses"])

        status1, status2, status3, status4 = statuses_list

        self.assertTrue(response.status_code == 200)
        self.assertTrue(status1.id == 1)
        self.assertTrue(status1.name == "In progress")

        self.assertTrue(status2.id == 2)
        self.assertTrue(status2.name == "Testing")

        self.assertTrue(status3.id == 3)
        self.assertTrue(status3.name == "Статус")

        self.assertTrue(status4.id == 4)
        self.assertTrue(status4.name == "Status")

    def test_create_status(self):
        self.client.force_login(self.user1)

        new_status = {
            "name": "New Status",
        }
        response = self.client.post(reverse("statuses:create"), new_status, follow=True)

        created_status = Status.objects.get(pk=5)

        self.assertRedirects(response, "/statuses/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Status created successfully!"))
        self.assertTrue(created_status.id == 5)
        self.assertTrue(created_status.name == "New Status")

    def test_update_status(self):
        self.client.force_login(self.user1)

        status = self.status4
        updated_data = {
            "name": "One more status",
        }

        response = self.client.post(
            reverse("statuses:update", args=(status.id,)), updated_data, follow=True
        )

        updated_status = Status.objects.get(id=status.id)

        self.assertRedirects(response, "/statuses/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Status updated successfully!"))
        self.assertTrue(updated_status.name == "One more status")

    def test_delete_status(self):
        self.client.force_login(self.user1)

        with self.assertRaises(Exception):
            self.client.post(
                reverse("statuses:delete", args=(self.status4.id,)), follow=True
            )

        Task.objects.all().delete()
        response = self.client.post(
            reverse("statuses:delete", args=(self.status4.id,)), follow=True
        )

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(id=self.status4.id)

        self.assertRedirects(response, "/statuses/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Status deleted successfully!"))
