from django.urls import path
from movies.views import ListPage

app_name = 'movies'

urlpatterns = [
	path('', ListPage.as_view()),
]