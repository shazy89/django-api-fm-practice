from django.contrib import admin

# Register your models here.

from .models import Task # for more *

admin.site.register(Task)