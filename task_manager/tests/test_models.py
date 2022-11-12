import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import TaskType, Position, Task


class ModelTests(TestCase):
    def test_task_type_str(self):
        name = "TestTaskType"
        task_type = TaskType.objects.create(
            name=name,
        )

        self.assertEqual(str(task_type), name)

    def test_position_str(self):
        name = "TestPosition"
        position = Position.objects.create(
            name=name,
        )

        self.assertEqual(str(position), name)

    def test_worker_str(self):
        username = "johndoe"
        first_name = "John"
        last_name = "Doe"
        position = Position.objects.create(name="Developer")
        worker = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            position=position,
        )

        self.assertEqual(str(worker), f"{first_name} {last_name}")

    def test_worker_create(self):
        username = "janedoe"
        password = "password"
        first_name = "Jane"
        last_name = "Doe"
        position = Position.objects.create(name="QA")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            position=position,
        )

        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.position, position)

    def test_task_str(self):
        name = ("Very Important Task",)
        description = "Correct logo css"
        deadline = datetime.datetime.now()
        is_completed = False
        priority = 1
        task_type = TaskType.objects.create(name="Bug")

        task = Task.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            is_completed=is_completed,
            priority=priority,
            task_type=task_type,
        )

        self.assertEqual(str(task), f"{name} (Priority: {priority})")
