from django.db import models


# Create your models here.

class About(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.first_name


class Education(models.Model):
    university = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    start_year = models.CharField(max_length=10, blank=False, default="")
    end_year = models.CharField(max_length=10, blank=False, default="")

    def __str__(self):
        return self.degree


class Experience(models.Model):
    company_name = models.CharField(max_length=30, blank=False)
    position = models.CharField(max_length=30, blank=False)
    start_year = models.CharField(max_length=30, blank=False)
    end_year = models.CharField(max_length=30, blank=False)
    job_responsibility = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.company_name + " " + self.position


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False)
    project_link = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)

    def __str__(self):
        return self.project_name
