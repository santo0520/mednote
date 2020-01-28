from django.contrib import admin
from .models import AbbreviationList, Abbreviation, NoteText
# Register your models here.
admin.site.register(Abbreviation)
admin.site.register(AbbreviationList)
admin.site.register(NoteText)
