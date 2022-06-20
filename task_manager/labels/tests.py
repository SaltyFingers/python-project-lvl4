from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.labels.models import Label

# Create your tests here.
OK_CODE = 200

class TestLabels(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)
        self.label4 = Label.objects.get(pk=4)

    def test_labels_list(self):
        self.client.force_login(self.user1)

        response = self.client.get(reverse("labels:list"))
        labels_list = list(response.context["labels"])

        label1, label2, label3, label4 = labels_list

        self.assertTrue(response.status_code == OK_CODE)
        self.assertTrue(label1.id == 1)
        self.assertTrue(label1.name == "Important")

        self.assertTrue(label2.id == 2)
        self.assertTrue(label2.name == "Just label")

        self.assertTrue(label3.id == 3)
        self.assertTrue(label3.name == "Метка")

        self.assertTrue(label4.id == 4)
        self.assertTrue(label4.name == "LABEL")

    def test_create_labels(self):
        self.client.force_login(self.user1)

        new_label = {
            "name": "New Label",
        }
        response = self.client.post(reverse("labels:create"), new_label, follow=True)

        created_label = Label.objects.get(pk=5)

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label created successfully!"))
        self.assertTrue(created_label.id == 5)
        self.assertTrue(created_label.name == "New Label")

    def test_update_labels(self):
        self.client.force_login(self.user1)

        updated_data = {
            "name": "One more label",
        }

        response = self.client.post(
            reverse("labels:update", args=(self.label4.id,)), updated_data, follow=True
        )

        updated_label = Label.objects.get(id=self.label4.id)

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label updated successfully!"))
        self.assertTrue(updated_label.name == "One more label")

    def test_delete_labels(self):
        self.client.force_login(self.user1)

        # with self.assertRaises(Exception):
        #     self.client.post(reverse("statuses:delete", args=(self.status4.id,)),
        #                      follow=True)

        # Task.objects.all().delete()
        response = self.client.post(
            reverse("labels:delete", args=(self.label4.id,)), follow=True
        )

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(id=self.label4.id)

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label deleted successfully!"))
