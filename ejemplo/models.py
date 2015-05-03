from django.core.urlresolvers import reverse
from django.db import models

class Director(models.Model):
    dni = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Genre(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    description = models.CharField(max_length=60)

class Film(models.Model):
    #id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    main_actor = models.CharField(max_length=60)
    #headshot = models.ImageField(upload_to= '/tmp' )
    director = models.ForeignKey(Director)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})

class Review(models.Model):
    code = models.ForeignKey(Film)
    score = models.IntegerField
    description = models.CharField(max_length=200)

