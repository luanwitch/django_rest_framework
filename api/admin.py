from django.contrib import admin # type: ignore
from .models import Category

admin.site.register(Category)