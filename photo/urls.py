from django.urls import path
from .views import *

app_name = 'photo'

urlpatterns = [
    path('', AlbumListView.as_view(), name='index'),
    path('album/', AlbumListView.as_view(),  name='album_list'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
]