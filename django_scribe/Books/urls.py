from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.AllBooksAPI.as_view(), name='AllBooksAPI'),
]