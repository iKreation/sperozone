from django.db import models

# Create your models here.
class Ocorrencia(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	report_date = models.DateTimeField("Reportado em:")
	status = models.CharField(max_length = 50)
	lat = models.CharField(max_length=100)
	lon = models.CharField(max_length=100)


	def to_dict(self):
		return {"title": self.title, "description": self.description, "report_date":self.report_date.strftime('%Y-%m-%d %H:%M'), "status":self.status,"lat":self.lat, "lon":self.lon}

	def __unicode__(self):
		return self.title