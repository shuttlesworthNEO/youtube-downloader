# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import SongNameForm
from utlis.down_loader import downloader
# Create your views here.

def MainView(request):
    if request.method == "POST":
        form = SongNameForm(request.POST)
        if form.is_valid():
            argument = form.cleaned_data['song_name']
            downloader(argument)
    else:
        form = SongNameForm()

    return render(request, 'index.html', {'form' : form})