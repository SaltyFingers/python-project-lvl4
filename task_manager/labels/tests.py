from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label
from task_manager.users.models import User
from task_manager.tasks.models import Task

# Create your tests here.

OK_CODE = 200


class TestLabels(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)
        self.label4 = Label.objects.get(pk=5)

    def test_not_login_user_access(self):
        response = self.client.post(
            reverse("labels:list"), follow=True
        )

        self.assertRedirects(response, "/login/?next=/labels/")

    def test_labels_list(self):
        self.client.force_login(self.user1)

        response = self.client.get(reverse("labels:list"))
        labels_list = list(response.context["labels"])

        test_label1, test_label2, test_label3, test_label4 = labels_list

        self.assertTrue(response.status_code == OK_CODE)

        self.assertTrue(test_label1.id == self.label1.id)
        self.assertTrue(test_label1.name == self.label1.name)

        self.assertTrue(test_label2.id == self.label2.id)
        self.assertTrue(test_label2.name == self.label2.name)

        self.assertTrue(test_label3.id == self.label3.id)
        self.assertTrue(test_label3.name == self.label3.name)

        self.assertTrue(test_label4.id == self.label4.id)
        self.assertTrue(test_label4.name == self.label4.name)

    def test_create_labels(self):
        self.client.force_login(self.user1)

        new_label = {
            "name": "New Label",
        }
        response = self.client.post(reverse("labels:create"),
                                    new_label, follow=True)

        created_label = Label.objects.last()
        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label created successfully!"))
        self.assertTrue(created_label.id == 6)
        self.assertTrue(created_label.name == "New Label")

    def test_update_labels(self):
        self.client.force_login(self.user1)

        updated_data = {
            "name": "One more label",
        }

        response = self.client.post(
            reverse("labels:update", args=(self.label4.id,)),
            updated_data,
            follow=True
        )

        updated_label = Label.objects.get(id=self.label4.id)

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label updated successfully!"))
        self.assertTrue(updated_label.name == "One more label")

    def test_delete_labels(self):
        self.client.force_login(self.user1)

        Task.objects.all().delete()

        response = self.client.post(
            reverse("labels:delete", args=(self.label4.id,)), follow=True
        )

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(id=self.label4.id)

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("Label deleted successfully!"))

    def test_delete_label_in_use(self):
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse("labels:delete", args=(self.label4.id,)), follow=True
        )

        self.assertRedirects(response, "/labels/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response,
                            _("Label can not be deleted\
                              because it is in use"))
