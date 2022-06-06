from django.db import models

# Create your models here.

class InputModel(models.Model):

	title = models.CharField(max_length=200, default='')
	description = models.TextField(default='')
	pdf = models.FileField(upload_to='pdfs/')

	def __str__(self):
		return self.title


class PdfModel(models.Model):
	choose_file = models.FileField(upload_to ='Pdf_uploads/', max_length=254, default='')

