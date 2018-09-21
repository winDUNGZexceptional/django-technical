from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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


	def post(self, request, *args, **kwargs):
		messages.success(request, 'Movie successfully added.')
		return HttpResponseRedirect( reverse('movies:list') )
