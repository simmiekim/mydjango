from django.urls import path
# from . import views
# urlpatterns = [
    # path('', views.my_view)
# ]

# from about.views import MyView
# urlpatterns = [
#     path('', MyView.as_view())
# ]

from about.views import AboutView
urlpatterns = [
    path('', AboutView.as_view())
]