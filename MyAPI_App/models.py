from django.db import models

# Create your models here.

# this is the repository model that I'm gonna use to store 
# the data returned by the API, I kept only relevant informations
class Repository(models.Model):
    # the name of the repo so that I can list the repositories by their names
    name = models.CharField(max_length=200, blank=False, unique=True)
    # the language used to develop the repo
    language = models.CharField(max_length=20, blank=False)
    # url of the repo
    url = models.CharField(max_length=255, default=None)

    # this will be useful on the dashboard admin for example
    def __str__(self):
        return self.name
