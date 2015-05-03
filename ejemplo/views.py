from django.core import urlresolvers
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.template import Template

from django.db.models import Q

from models import Film,Genre,Director,Review
from forms import FilmForm

import os
# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template( 'template2.html' )
    su = ["cosa1","cosa2"]
    html = t.render(Context({ 'current_date' : now , 'cosa' : su}))
    return HttpResponse(html)

'''def current_datetime(request):
    now = datetime.datetime.now()
    RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))
    path =  os.path.join(RUTA_PROYECTO, 'templates')
    html = " <html><body>It is now %s .y el path es path %s</body></html> " % (now,path)
    return HttpResponse(html)'''


def delete_movie(request):
    pass

#class intro_director()

class intro_review(CreateView):
    pass

def review(request, pk):
    film = get_object_or_404(Film, pk=pk)
    new_review = Review(
        code=film,
        score=request.POST['score'],
        description=request.POST['description'])
    new_review.save()
    return HttpResponseRedirect(urlresolvers.reverse('ejemplo:film_detail', args=(film.id,)))

class intro_movie(CreateView):
    model = Film
    template_name = 'form.html'
    form_class = FilmForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(intro_movie, self).form_valid(form)

def filmList(request):
    films = Film.objects.all()
    t = get_template('formFilmList.html')
    return HttpResponse(t.render(Context({'film_list':films})))

def filmGenre(request,pk):
    films = Film.objects.filter(genre=pk)
    t = get_template('formFilmList.html')
    return HttpResponse(t.render(Context({'film_list':films})))

'''class FilmGenre(DetailView):

    context_object_name = 'filmForGenre'
    queryset = Film.objects.get(Genre)'''

def movies(request, pk):
    idd = int(pk)
    f = Film.objects.filter(Country='EEUU')
    t = get_template('concretFilm.html')
    return HttpResponse(t.render(Context({'cfilmf':f})))

class FilmDetail(DetailView):
    model = Film
    template_name = 'concretFilm.html'

    def get_context_data(self, **kwargs):
        context = super(FilmDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context




def directorList(request):
    directors = Film.objects.all()
    t = get_template('formFilmList.html')
    return HttpResponse(t.render(Context({'list_director':directors})))


def top_rated(request):
    pass


