from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from courses.models import Course
from .models import Batch


class BatchCreatePermissionTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python Full Stack',
            short_description='Learn the stack',
            description='A complete program.',
            duration='12 weeks',
            fees=15000,
        )
        self.create_url = reverse('batch_create')
        self.list_url = reverse('batch_list')
        self.student = User.objects.create_user(
            username='student',
            password='pass12345',
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass12345',
        )
        self.staff.user_permissions.add(
            Permission.objects.get(codename='add_batch')
        )

    def test_create_batch_hidden_without_permission(self):
        self.client.login(username='student', password='pass12345')
        response = self.client.get(self.list_url)
        self.assertNotContains(response, 'Create batch')
        self.assertEqual(self.client.get(self.create_url).status_code, 403)

    def test_create_batch_visible_with_permission(self):
        self.client.login(username='staff', password='pass12345')
        response = self.client.get(self.list_url)
        self.assertContains(response, reverse('batch_create'))

    def test_staff_can_create_batch(self):
        self.client.login(username='staff', password='pass12345')
        response = self.client.post(
            self.create_url,
            {
                'name': 'April weekday',
                'course': self.course.pk,
                'start_date': '2026-04-01',
                'end_date': '2026-06-30',
                'schedule': 'Mon–Fri, 7–9 PM',
                'duration': '12 weeks',
                'instructor': 'ZS Mentor',
                'students_count': '0',
                'status': 'upcoming',
                'description': 'New cohort',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Batch.objects.filter(name='April weekday').exists())
