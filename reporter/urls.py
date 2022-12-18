from django.urls import path
from . import views


urlpatterns = [
    path("reporter", views.reporter, name="reporter"), # Path for the reporter's page
    path("admin", views.admin, name="admin"), # Path for the registration and login page
    path("register", views.register, name="register"), # Path for the registration form
    path("login", views.login, name="login"), # Path for the login form
    path("logout", views.logout, name="logout"), # Log out path 
    path("article_form", views.article_form, name="article_form"), # Path for the article form 
    path("article", views.article, name="article") # Path for article page
]
