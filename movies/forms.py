from django import forms

from movies.models import Movie

class AddMovieForm(forms.ModelForm):

	title = forms.CharField(
		max_length = 100,
		help_text = 'upto 100 characters only.'
		)

	description = forms.CharField(
		widget = forms.Textarea,
		help_text = 'The summary of the movie.'
		)

	director = forms.CharField(max_length=100)

	date_screened = forms.DateField(
		# widget = forms.widgets.DateInput(format="%m-%d-%Y"),
		input_formats = ("%m-%d-%Y", "%m/%d/%Y"),
		help_text = "MM-DD-YYYY"
		)

	class Meta:

		model = Movie

		fields = ('title', 'description', 'director', 'date_screened',)