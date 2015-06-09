from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Film, Genre, Director, FilmReview


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')
        groups = CharField(read_only=True)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='film-detail')
    # filmreview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='restaurantreview-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Film
        fields = ('url', 'title', 'country', 'city', 'main_actor', 'director', 'genre', 'user')


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='director-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Director
        fields = ('url', 'first_name', 'last_name', 'user')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='genre-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Genre
        fields = ('url', 'name', 'description', 'user')


class FilmReviewSerializer(serializers.HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='filmreview-detail')
    film = HyperlinkedRelatedField(view_name='film-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = FilmReview
        fields = ('url', 'rating', 'comment', 'user', 'date', 'film')