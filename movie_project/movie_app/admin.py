from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db.models import QuerySet
from django.contrib.auth.models import User
from .models import Director


# Register your models here.
@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    list_editable = ['first_name', 'last_name', 'email']
