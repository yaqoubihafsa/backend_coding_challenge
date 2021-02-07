from django.contrib import admin
from .models import Repository

# Register your models here.

# to get access through the dashboard
admin.site.register(Repository)

