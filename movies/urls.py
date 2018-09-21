from django.urls import path
from movies.views import ListPage, AddPage

app_name = 'movies'

urlpatterns = [
	path('', ListPage.as_view()),
	path('list/', ListPage.as_view()),
	path('add/', AddPage.as_view()),
]