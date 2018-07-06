from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogIndex.as_view(), name="index"),

]
