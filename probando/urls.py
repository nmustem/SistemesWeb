from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView, UpdateView, DeleteView
from ejemplo.views import directorFilms,filmList,directorList, FilmDetail,GenreDetail,DirectorDetail,filmGenre,genreList, \
    mainPage

urlpatterns = [
    # Examples:

    url(r'^$',mainPage,  name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),




    # url(r'^intro/$',
    #     intro_movie.as_view(),
    #     name='film_intro'),

    #url(r'^movie/(?P<pk>\d+)/$ ', movies, name='info_film' ),

    #FILM
    url(r'^film/$',
        filmList.as_view(),
        name='film_list'),

    url(r'^film\.(?P<extension>(json|xml))$',
        filmList.as_view(),
        name='film_list_extension'),

    url(r'^film/(?P<pk>\d+)/$',
        FilmDetail.as_view(),
        name='film_detail'),

    url(r'^film/(?P<pk>\d+)\.(?P<extension>(json|xml))$$',
        FilmDetail.as_view(),
        name='film_detail_extension'),



    #DIRECTOR
    url(r'^director/$',
        directorList.as_view(),
        name='director_list' ),

    url(r'^director\.(?P<extension>(json|xml))$',
        directorList.as_view(),
        name='director_list_extension' ),

    url(r'^director/(?P<pk>\d+)/$',
        DirectorDetail.as_view(),
        name='director_detail',
        ),

    url(r'^director/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        DirectorDetail.as_view(),
        name='director_detail_extension',
        ),

    url(r'^director/(?P<pk>\d+)/films/$',
        directorFilms,
        name='director_list_films' ),



    ##GENRE
    url(r'^genre/$',
        genreList.as_view(),
        name='genre_list',
        ),

    url(r'^genre\.(?P<extension>(json|xml))$',
        genreList.as_view(),
        name='genre_list_extension',
        ),

    url(r'^genre/(?P<pk>\d+)/$',
        GenreDetail.as_view(),
        name='genre_detail',
        ),

    url(r'^genre/(?P<pk>\d+)\.(?P<extension>(json|xml))$',
        GenreDetail.as_view(),
        name='genre_detail_extension',
        ),

    url(r'^genre/(?P<pk>\d+)/films/$',
        filmGenre,
        name='film_genre'),


]