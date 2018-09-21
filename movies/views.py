from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class ListPage(View):

	template_name = 'movies/pages/list.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})