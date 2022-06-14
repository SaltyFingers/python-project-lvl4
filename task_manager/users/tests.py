from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

# Create your tests here.

class TestUsers(TestCase):


    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']


    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
        self.status4 = Status.objects.get(pk=4)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label2 = Label.objects.get(pk=3)


    def test_users_list(self):
        pass
    
    
    def test_create_user(self):
        new_user = {
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'username': 'Username',
            'password1': 'qwerty12345',
            'password2': 'qwerty12345',
        }
        response = self.client.post('users:create', new_user)
        
        self.assertRedirects(response, '/login')

        self.assertContains(response, 'User created successfully!')

        created_new_user = User.objects.get(pk=4)

        self.assertTrue(created_new_user.check_password('qwerty12345'))
        self.assertTrue(created_new_user.username=='Username')


    def test_update_user(self):
        pass


    def test_delete_user(self):
        pass
