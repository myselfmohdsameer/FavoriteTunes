from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Artist, Song
from .forms import ArtistForm, SongForm

class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'

class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'

class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'song_form.html'
    success_url = '/songs/'

class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'

class ArtistSongListView(ListView):
    model = Song
    template_name = 'artist_song_list.html'
    context_object_name = 'songs'

    def get_queryset(self):
        artist_id = self.kwargs['pk']
        return Song.objects.filter(artist__id=artist_id)
