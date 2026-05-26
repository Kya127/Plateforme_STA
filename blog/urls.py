from django.urls import path
from .views import NoteCreateview,SignUpView,NoteListeView,NoteDetailView,NoteUpdateView,NoteDeleteView
from .views import HomeView,MesNotesView
urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    path ('notes/', NoteCreateview.as_view(), name='mesnotes'),
    path('inscription', SignUpView.as_view(), name='signup'),
    path('liste_notes',NoteListeView.as_view(),name='liste_notes'),
    path('detail_note/<int:pk>',NoteDetailView.as_view(),name='detailsnotes'),
    path('modifier_note/<int:pk>',NoteUpdateView.as_view(),name='updatenote'),
    path('supprimer_note/<int:pk>',NoteDeleteView.as_view(),name='deletenote'),
    path('mes_notes', MesNotesView.as_view(), name='mes_notes'),
]
