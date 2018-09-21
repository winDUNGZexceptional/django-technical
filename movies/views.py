from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from movies.forms import AddMovieForm
from movies.models import Movie

# Create your views here.


class ListPage(View):

	template_name = 'movies/pages/list.html'

	def get(self, request, *args, **kwargs):
		movie_list = Movie.objects.filter(is_active=True)
		return render(request, self.template_name, {'movies' : movie_list})



class DetailPage(View):
	
	template_name = 'movies/pages/details.html'

	def get(self, request, *args, **kwargs):
		movie = Movie.objects.filter(id=self.kwargs['movie_id']).first()
		return render(request, self.template_name, {'movie' : movie})



class AddPage(CreateView):

	model = Movie
	template_name = 'movies/pages/add.html'
	form_class = AddMovieForm
	success_url = reverse_lazy('movies:list')

	def get_success_url(self, **kwargs):
		messages.success(self.request, 'Movie successfully added.')
		return self.success_url


