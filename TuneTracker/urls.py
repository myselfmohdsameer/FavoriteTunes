from django.urls import path
from .views import SongListView, SongDetailView, ArtistListView, ArtistSongListView, SongCreateView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='song_list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song_detail'),
    path('artists/', ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/songs/', ArtistSongListView.as_view(), name='artist_song_list'),
    path('songs/add/', SongCreateView.as_view(), name='song_add'),
]
