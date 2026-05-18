from django.contrib import admin
from .models import Categorie, Note


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)
admin.site.register(Categorie,CategorieAdmin)    

class NoteAdmin(admin.ModelAdmin):
    list_display = ('titre','contenu','date_entree')
    search_fields = ('titre',)
    list_filter = ('titre','date_entree')

    

admin.site.register(Note,NoteAdmin)
