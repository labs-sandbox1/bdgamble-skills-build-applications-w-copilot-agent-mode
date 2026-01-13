from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='Test Description')
    
    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(str(self.team), 'Test Team')


class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team=self.team,
            is_superhero=True
        )
    
    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.is_superhero)
        self.assertEqual(str(self.user), 'Test User')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            team=self.team
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Running',
            duration=30,
            date=date.today()
        )
    
    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)


class TeamAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='Test Description')
    
    def test_get_teams(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'New Team', 'description': 'New Description'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
    
    def test_get_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
