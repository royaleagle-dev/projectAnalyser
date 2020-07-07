from django.db import models
from django.utils import timezone

class Project (models.Model):
	'''Representing a particular project e.g facebook clone project'''
	name = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500, help_text = "limit to 500 chars")
	completed = models.BooleanField(default = False)
	startDate = models.DateTimeField(default = timezone.now, blank = True, null = True)
	endDate = models.DateTimeField(blank = True, null = True)
	developer = models.CharField(max_length = 100)

	def __str__(self):
		return self.name