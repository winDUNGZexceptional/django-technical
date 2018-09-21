from django.db import models

# Create your models here.


class Movie(models.Model):

	title = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	description = models.TextField()
	likes = models.PositiveIntegerField(default=0)

	date_screened = models.DateField()

	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)


