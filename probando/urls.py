from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import ListView, UpdateView, DeleteView
from rest_framework.urlpatterns import format_suffix_patterns
from ejemplo.views import directorFilms,filmList,directorList, FilmDetail,GenreDetail,DirectorDetail,filmGenre,genreList, \
    mainPage,intro_movie,APIFilmList,APIFilmDetail,APIDirectorDetail,APIDirectorList, APIGenreList, APIGenreDetail,register, \
    review, APIFilmReviewList, APIFilmReviewDetail

urlpatterns = [
    # Examples:

    url(r'^$',mainPage,  name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$',
        register,
        name='register'),

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

    url(r'^film/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),



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





    url(r'^films/intro$',
        intro_movie.as_view(),
        name='film-intro'),


]

##########API URLS
urlpatterns += patterns('',
	url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/films/$', APIFilmList.as_view(), name='film-list'),
    url(r'^api/films/(?P<pk>\d+)/$', APIFilmDetail.as_view(), name='film-detail'),
    url(r'^api/filmreviews/$', APIFilmReviewList.as_view(), name='filmreview-list'),
	url(r'^api/filmreviews/(?P<pk>\d+)/$', APIFilmReviewDetail.as_view(), name='filmreview-detail'),
    url(r'^api/directors/$',APIDirectorList.as_view(),name='director-list'),
    url(r'^api/directors/(?P<pk>\d+)/$',APIDirectorDetail.as_view(),name='director-detail'),
    url(r'^api/genres/$' ,APIGenreList.as_view(), name='genre-list'),
    url(r'^api/genres/(?P<pk>\d+)/$',APIGenreDetail.as_view(),name='genre-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])