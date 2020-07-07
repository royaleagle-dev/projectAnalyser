from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
	path('', views.ProjectListView.as_view(), name = 'index'),
	path('details/<int:pk>/', views.ProjectDetailView.as_view(), name = 'details'),
	path('about/', views.about, name = 'about')
]