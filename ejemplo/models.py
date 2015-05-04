
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now



#//////cambiar director_list de reverse

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):
        return u"%s" % self.first_name+' '+self.last_name

    def get_absolute_url(self):
        return reverse('film_list', kwargs={'pk': self.pk})

class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)

    def __unicode__(self):
        return u"%s" % self.name

class Film(models.Model):
    title = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    main_actor = models.CharField(max_length=60)
    #headshot = models.ImageField(upload_to= '/tmp' )
    director = models.ForeignKey(Director)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'pk': self.pk})

class Review(models.Model):
    film = models.ForeignKey(Film)
    score = models.IntegerField
    description = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('film_list', kwargs={'pk': self.pk})

