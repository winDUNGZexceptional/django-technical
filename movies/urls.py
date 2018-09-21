from django.urls import path
from movies.views import ListPage, AddPage, DetailPage

app_name = 'movies'

urlpatterns = [
	path('', ListPage.as_view(), name='list'),
	path('list/', ListPage.as_view()),
	path('<int:movie_id>/', DetailPage.as_view(), name='details'),
	path('add/', AddPage.as_view(), name='add'),
]