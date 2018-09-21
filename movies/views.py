from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from movies.forms import AddMovieForm

# Create your views here.


class ListPage(View):

	template_name = 'movies/pages/list.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})


class AddPage(View):

	template_name = 'movies/pages/add.html'

	def get(self, request, *args, **kwargs):

		form = AddMovieForm(label_suffix = ': ')

		return render(request, self.template_name, {'form' : form})

