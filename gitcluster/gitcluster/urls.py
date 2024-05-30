from django.contrib import admin
from django.urls import path
from gitclusterapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('github-connect/', views.github_connect, name='github_connect'),
]
