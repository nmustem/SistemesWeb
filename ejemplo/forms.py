from django.forms import ModelForm,models
from ejemplo.models import Director,Film,Review,Genre

'''from django import newforms as forms
TOPIC_CHOICES = (
('general' , 'General enquiry'),
('bug','Bug report'),
( 'suggestion','Suggestion'),
)
class ContactForm(forms.Form):
topic = forms.ChoiceField(choices=TOPIC_CHOICES)
message = forms.CharField()
sender = forms.EmailField(required=False)'''

class FilmForm(ModelForm):
    class Meta:
        model = Film
        #fields = ['title','country','city','main_actor','director','genre']
        exclude = ('user', 'date',)

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['dni', 'first_name', 'last_name','email']
        exclude = ('film','user', 'date',)

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'description']
        exclude = ('director','film','user', 'date',)