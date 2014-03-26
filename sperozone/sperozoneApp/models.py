from django.db import models

# Create your models here.
class Ocorrencia(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	report_date = models.DateTimeField("Reportado em:")
	status = models.CharField(max_length = 50)


	def __unicode__(self):
		return self.title