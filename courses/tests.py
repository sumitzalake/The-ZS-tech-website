from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse

from .models import Course


class CourseCreatePermissionTests(TestCase):
    def setUp(self):
        self.create_url = reverse('course_create')
        self.list_url = reverse('course_list')
        self.student = User.objects.create_user(
            username='student',
            password='pass12345',
        )
        self.staff = User.objects.create_user(
            username='staff',
            password='pass12345',
        )
        self.staff.user_permissions.add(
            Permission.objects.get(codename='add_course')
        )

    def test_add_course_hidden_without_permission(self):
        self.client.login(username='student', password='pass12345')
        response = self.client.get(self.list_url)
        self.assertNotContains(response, 'Add course')
        self.assertEqual(self.client.get(self.create_url).status_code, 403)

    def test_add_course_visible_with_permission(self):
        self.client.login(username='staff', password='pass12345')
        response = self.client.get(self.list_url)
        self.assertContains(response, reverse('course_create'))

    def test_staff_can_create_course(self):
        self.client.login(username='staff', password='pass12345')
        response = self.client.post(
            self.create_url,
            {
                'title': 'Python Full Stack',
                'short_description': 'Learn the stack',
                'description': 'A complete program.',
                'duration': '12 weeks',
                'fees': '15000',
                'is_active': 'on',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Course.objects.filter(title='Python Full Stack').exists())
