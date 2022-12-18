from django.urls import path
from . import views
from reporter.models import Article


urlpatterns = [
    path("", views.news), # Path for the news page
    path("view/<int:id>", views.news_view, name='view'), # Path for the news details to view
    path("female", views.female, name="female"), # Path for female news page
    path("male", views.male, name="male"), # Path for the male news page
    path("world_cup", views.world_cup, name="world_cup") # Path for the world cup news page
]