from django import forms

class SongNameForm(forms.Form):
    song_name = forms.CharField(max_length=None)