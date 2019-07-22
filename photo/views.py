from django.shortcuts import render

from django.views.generic import ListView, DetailView
from photo.models import Album, Photo

class AlbumListView(ListView):
    model = Album

class AlbumDetailView(DetailView):
    model = Album

class PhotoDetailView(DetailView):
    model = Photo
