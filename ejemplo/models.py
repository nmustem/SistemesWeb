
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from datetime import date

class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.first_name+' '+self.last_name

    def get_absolute_url(self):
        return reverse('director-detail', kwargs={'pk': self.pk})

class Genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    user = models.ForeignKey(User, default=1)

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
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('film-detail', kwargs={'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=2, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class FilmReview(Review):
    film = models.ForeignKey(Film)

    def __unicode__(self):
        return u"%s" % self.film