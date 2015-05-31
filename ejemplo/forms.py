from django.forms import ModelForm,models
from ejemplo.models import Director,Film,Genre

class FilmForm(ModelForm):
    class Meta:
        model = Film
        #fields = ['title','country','city','main_actor','director','genre']
        exclude = ('user', 'date',)

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['first_name', 'last_name']
        #exclude = ('film','user', 'date',)

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        exclude = ('director','film','user', 'date',)