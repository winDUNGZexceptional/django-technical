from django import forms

class AddMovieForm(forms.Form):

	title = forms.SlugField(
		max_length = 100,
		help_text = 'upto 100 characters only.'
		)
	description = forms.CharField(
		widget = forms.Textarea,
		help_text = 'The summary of the movie.'
		)
	director = forms.SlugField(max_length=100)

	date_screened = forms.DateField()
