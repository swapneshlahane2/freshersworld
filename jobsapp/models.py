from django.db import models

# Create your models here.
class SoftwareJobs(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    vaccancy = models.IntegerField()
    experience = models.FloatField()
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class PharmaJobs(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    vaccancy = models.IntegerField()
    experience = models.FloatField()
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class AgricultureJobs(models.Model):
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    vaccancy = models.IntegerField()
    experience = models.FloatField()
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
