from django import forms

class SongNameForm(forms.ModelForm):
    song_name = forms.CharField(max_length=None)

    class Meta:
        fields = ['song_name',]