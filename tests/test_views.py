from project.models import Project
from django.test import TestCase
from django.urls import reverse
import datetime
from django.utils import timezone

def createProject(name, description, completed, developer):
	startDate = timezone.now()
	endDate = timezone.now() + datetime.timedelta(days = 5)
	return Project.objects.create(name = name, description = description, completed = completed, startDate = startDate, endDate = endDate, developer= developer)

class ProjectIndexViewTest(TestCase):
	
	def test_no_projects(self):
		response = self.client.get(reverse('project:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['projects']['all'], [])

	def test_one_project(self):
		createProject('BlueBook', 'A blue book', False, 'Ayotunde Okunubi')
		response = self.client.get(reverse('project:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['projects']['all'], ['<Project: BlueBook>'])

	def test_multiple_project(self):
		createProject('Test', 'A test project', True, 'Olaoluwapo Okunubi')
		createProject('Test2', 'A second test', False, 'Ayotunde Okunubi')
		response = self.client.get(reverse('project:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(response.context['projects']['all'], ['<Project: Test>', '<Project: Test2>'])

class ProjectDetailViewTest(TestCase):

	def test_detail_success(self):
		project = createProject('BlueBook', 'my blue book', True, 'Ayotunde Okunubi')
		url = reverse('project:details', args = (project.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)