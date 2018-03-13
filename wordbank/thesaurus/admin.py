from django.contrib import admin
from .models import Word, Synonym

# Register your models here.

admin.site.register(Word)
admin.site.register(Synonym)