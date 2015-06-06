from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import urlresolvers
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from django.template import Template

from django.db.models import Q
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings
from ejemplo.serializers import UserSerializer,FilmSerializer, DirectorSerializer, GenreSerializer
from rest_framework import generics, permissions
from django.views.generic.edit import CreateView, UpdateView

from models import Film,Genre,Director, FilmReview
from forms import FilmForm

from django.core import serializers

from rest_framework import status

import os
# Create your views here.

class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        else:
            return super(ConnegResponseMixin, self).render_to_response(context)

#class intro_director()

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API
    """
    return Response({
        'users': reverse('user-list', vrequest=request),
        'groups': reverse('group-list', request=request),
    })


class UserList(generics.ListCreateAPIView):
    """
      API endpoint that	represents a list of users
    """
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myrestaurants/form.html'


# class intro_review(CreateView):
#     pass

# '''def review(request, pk):
#     film = get_object_or_404(Film, pk=pk)
#     new_review = Review(
#         code=film,
#         score=request.POST['score'],
#         description=request.POST['description'])
#     new_review.save()
#     return HttpResponseRedirect(urlresolvers.reverse('ejemplo:film_detail', args=(film.id,)))'''

class intro_movie(CreateView):
    model = Film
    template_name = 'form.html'
    form_class = FilmForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(intro_movie, self).form_valid(form)


# def filmList(request):
#     films = Film.objects.all()
#     t = get_template('formFilmList.html')
#     return HttpResponse(t.render(Context({'film_list':films})))

def mainPage(request):
    t = get_template('mainPage.html')
    return HttpResponse(t.render(Context({})))

class filmList(ListView, ConnegResponseMixin):
    model = Film
    queryset = Film.objects.all()
    context_object_name = 'film_list'
    template_name = 'formFilmList.html'

def filmGenre(request,pk):
    films = Film.objects.filter(genre=pk)
    t = get_template('formFilmList.html')
    return HttpResponse(t.render(Context({'film_list':films})))

def directorFilms(request,pk):
    films = Film.objects.filter(director=pk)
    t = get_template('formFilmList.html')
    return HttpResponse(t.render(Context({'film_list':films})))

    # def filmDirector(request,pk):
    # pk = str(pk)
    # direct = Director.objects.filter(first_name=pk)
    # director = Film.objects.filter(director=direct.dni)
    # t = get_template('formFilmList.html')
    # return HttpResponse(t.render(Context({'film_list':director})))
    #
    # class FilmGenre(DetailView):
    #
    # context_object_name = 'filmForGenre'
    # queryset = Film.objects.get(Genre)

# def movies(request, pk):
#     idd = int(pk)
#     f = Film.objects.filter(Country='EEUU')
#     t = get_template('concretFilm.html')
#     return HttpResponse(t.render(Context({'cfilmf':f})))

class FilmDetail(DetailView, ConnegResponseMixin):
    model = Film
    template_name = 'concretFilm.html'

    def get_context_data(self, **kwargs):
        context = super(FilmDetail, self).get_context_data(**kwargs)
        return context

class GenreDetail(DetailView, ConnegResponseMixin):
    model = Genre
    template_name = 'concretGenre.html'

    def get_context_data(self, **kwargs):
        context = super(GenreDetail, self).get_context_data(**kwargs)
        return context

class DirectorDetail(DetailView, ConnegResponseMixin):
    model = Director
    template_name = 'concretDirector.html'

    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        return context



# def directorList(request, ConnegResponseMixin):
#     directors = Director.objects.all()
#     t = get_template('formDirectorList.html')
#     resp = t.render(Context({'list_director':directors}))
#     print resp
#     return HttpResponse(resp)

class directorList(ListView, ConnegResponseMixin):
    model = Film
    queryset = Director.objects.all()
    context_object_name = 'list_director'
    template_name = 'formDirectorList.html'


class genreList(ListView, ConnegResponseMixin):
    model = Genre
    queryset = Genre.objects.all()
    context_object_name = 'list_genre'
    template_name = 'GenreList.html'

# def genreList(request, ConnegResponseMixin):
#     genres = Genre.objects.all()
#     t = get_template('GenreList.html')
#     resp = t.render(Context({'list_genre':genres}))
#     return HttpResponse(resp)

def top_rated(request):
    pass

@login_required()
def review(request, pk):
    film = get_object_or_404(Film, pk=pk)
    new_review = FilmReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        film= film)
    new_review.save()
    return HttpResponseRedirect(urlresolvers.reverse('film_detail', args=(film.id,)))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

#RESTful API views

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class APIFilmList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Film
    queryset = Film.objects.all()

    serializer_class = FilmSerializer

class APIFilmDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    model = Film
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class APIDirectorList(generics.ListCreateAPIView):
    permissions_classes = (IsAuthenticatedOrReadOnly,)
    model = Director
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class APIDirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    permissions_classes = (IsAuthenticatedOrReadOnly,)
    model = Director
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class APIGenreList(generics.ListAPIView):
    permissions_classes = (IsAuthenticatedOrReadOnly,)
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class APIGenreDetail(generics.RetrieveAPIView):
    permissions_classes = (IsAuthenticatedOrReadOnly,)
    model = Genre
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



