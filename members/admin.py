from django.contrib import admin
from .models import Poost

@admin.register(Poost)
class PoostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'author')