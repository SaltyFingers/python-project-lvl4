from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task
from task_manager.users.models import User

# Create your tests here.
OK_CODE = 200


class TestUsers(TestCase):

    fixtures = ["users.json", "statuses.json", "tasks.json", "labels.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_users_list(self):
        response = self.client.get(reverse("users:list"))
        users_list = list(response.context["users"])

        test_user1, test_user2, test_user3 = users_list

        self.assertTrue(response.status_code == OK_CODE)
        self.assertTrue(test_user1.id == self.user1.id)
        self.assertTrue(test_user1.username == self.user1.username)

        self.assertTrue(test_user2.id == self.user2.id)
        self.assertTrue(test_user2.username == self.user2.username)

        self.assertTrue(test_user3.id == self.user3.id)
        self.assertTrue(test_user3.username == self.user3.username)

    def test_create_user(self):
        new_user = {
            "first_name": "Firstname",
            "last_name": "Lastname",
            "username": "Username",
            "password1": "qwerty12345",
            "password2": "qwerty12345",
        }
        response = self.client.post(reverse("users:create"),
                                    new_user, follow=True)

        created_user = User.objects.last()

        self.assertRedirects(response, "/login/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("User created successfully!"))
        self.assertTrue(created_user.check_password("qwerty12345"))
        self.assertTrue(created_user.username == "Username")
        self.assertTrue(created_user.id == 4)

    def test_update_user(self):
        user = self.user1
        updated_data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": "NewUsername",
            "password1": "54321ytrewq",
            "password2": "54321ytrewq",
        }
        self.client.force_login(user)
        old_username = user.username
        old_id = user.id

        response = self.client.post(
            reverse("users:update", args=(user.id,)), updated_data, follow=True
        )

        updated_user = User.objects.get(id=user.id)

        self.assertRedirects(response, "/users/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("User updated successfully!"))
        self.assertFalse(updated_user.username == old_username)
        self.assertTrue(updated_user.username == "NewUsername")
        self.assertTrue(updated_user.id == old_id)
        self.assertTrue(updated_user.check_password("54321ytrewq"))

    def test_delete_user(self):
        self.client.force_login(self.user1)

        with self.assertRaises(Exception):
            self.client.post(
                reverse("users:delete", args=(self.user1.id,)), follow=True
            )

        Task.objects.all().delete()
        response = self.client.post(
            reverse("users:delete", args=(self.user1.id,)), follow=True
        )

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user1.id)

        self.assertRedirects(response, "/users/")
        self.assertTrue(response.status_code == OK_CODE)
        self.assertContains(response, _("User deleted successfully!"))
