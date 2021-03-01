from django.db import models
from django.contrib.auth.models import AbstractUser


# class model names are SINGULAR 
# make decision about the User early 
# you can change models later, don't want to change the user one 

class User(AbstractUser):
    pass

class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.CharField(max_length=75)
    release_date = models.IntegerField(blank=True, null=True)
    # one to many relationship, using the foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")

    # this change doesn't change the DB so no mirgrations are needed 
    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    label = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

