# myapp/admin.py
from django.contrib import admin
from .models import Repository

admin.site.register(Repository)
