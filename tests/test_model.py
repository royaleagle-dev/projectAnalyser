from django.test import TestCase
from project.models import Project
from django.utils import timezone

def createProject(name, description, completed, startDate, endDate, developer):
	return Project.objects.create(name = name, description = description, completed = completed, startDate = startDate, endDate = endDate, developer=developer)

class ProjectTest(TestCase):
	def setUp(self):
		createProject('Test Project', 'a project for testing', False, timezone.now(), timezone.now() + timezone.timedelta(days =8), 'Ayotunde Okunubi' )
		createProject('Test Project2', 'a second testing project', True, timezone.now(), timezone.now() + timezone.timedelta(days =5), 'Olaolu Okunubi')

	def test_projectRetrunStr(self):
		project = Project.objects.get(id = 1)
		project2 = Project.objects.get(id = 2)
		self.assertEqual(str(project), 'Test Project')
		self.assertEqual(str(project2), 'Test Project2')