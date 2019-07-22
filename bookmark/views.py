from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Bookmark

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark


