from django.test import TestCase
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.utils import IntegrityError
from .models import *

# Create your tests here.

class TaskModelTests(TestCase):

    def test_creation_task(self):

        task = BillTask.objects.create(title = "test for creation of task",
                                      description = "verifying if an object task is created",
                                      status = "Not Completed")

        self.assertEqual(task.title, 'test for creation of task')
        self.assertEqual(task.description, 'verifying if an object task is created')


    def test_update_status(self):

        self.task.status = 'Completed'
        self.task.save()

        self.assertEqual(self.task.status, 'Completed')

    def test_delete_task(self):
        num_task_before = BillTask.objects.count()

        self.task.delete()

        num_task_after = BillTask.objects.count()

        self.assertEqual(num_task_before - 1, num_task_after)

    def test_delete_nonexistent_task(self):
        self.task.delete()

        with self.assertRaises(ObjectDoesNotExist):
            self.task.delete()
            