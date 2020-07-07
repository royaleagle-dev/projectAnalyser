from django.shortcuts import render
from project.models import Project
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProjectListView(ListView):
	model = Project
	context_object_name = 'projects'
	template_name = 'project/index.html'

	def get_queryset(self):
		queryset = {
			'all':Project.objects.all().order_by('id'),
			'completed':Project.objects.filter(completed__exact = True),
			'pending':Project.objects.filter(completed__exact = False),
		}
		return queryset

class ProjectDetailView(DetailView):
	model = Project
	context_object_name = 'project'
	template_name = 'project/detail.html'

def about(request):
	return render(request, 'project/about.html')
