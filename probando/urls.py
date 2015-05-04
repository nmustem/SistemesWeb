from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView, UpdateView, DeleteView
from ejemplo.forms import FilmForm
from ejemplo.models import Film, Genre
from ejemplo.views import current_datetime,intro_movie,filmList,movies,directorList, FilmDetail,filmGenre, genreList#, filmDirector

urlpatterns = [
    # Examples:
    # url(r'^$', 'probando.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$' , current_datetime),
    url(r'^intro/$',
        intro_movie.as_view(),
        name='film_intro'),
    #url(r'^film_list/$', filmList, name='film_list'),
    #url(r'^movie/(?P<pk>\d+)/$ ', movies, name='info_film' ),
    url(r'^director/$', directorList, name='director_list' ),

    url(r'^film/$',
        ListView.as_view(
            queryset=Film.objects.all(),
            context_object_name='film_list',
            template_name='formFilmList.html'),
        name='film_list'),

    url(r'^film/(?P<pk>\d+)/$',
        FilmDetail.as_view(),
        name='film_detail'),


    url(r'^film/(?P<pk>\d+)/delete$',
        DeleteView.as_view(
        model=Film,
        template_name='film_confirm_delete.html',
        #success_url=
        ), name='delete_film'),

    url(r'^film/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(
            model=Film,
            form_class=FilmForm,
            template_name='form.html'),
        name='restaurant_edit'),


    # url(r'^film/(?P<pk>\d+)/reviews/create/$',
    #     'ejemplo.views.review',
    #     name='review_create'),

    url(r'^film/genre/(?P<pk>[a-z]+)/$',
        filmGenre,
        name='film_genre'),

    url(r'^genre/$', genreList , name='genre_list' ),

    # url(r'^film/director/(?P<pk>[a-zA-Z]+)/$',
    #     filmDirector,
    #     name='film_director'),

]
