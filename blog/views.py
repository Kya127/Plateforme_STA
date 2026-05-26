from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView,TemplateView
from django.contrib.auth.views import LoginView
from .models import Categorie, Note
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



class HomeView(TemplateView):
    template_name = 'ui/home.html'

class NoteCreateview(LoginRequiredMixin,CreateView):
    model = Note
    template_name = 'notes.html'
    form_class = NoteForm
    success_url = reverse_lazy('liste_notes')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

    
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    

class NoteListeView(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'liste_note.html'
    context_object_name = 'liste_note'
    paginate_by = 6

    def get_queryset(self):
        queryset = Note.objects.all()

        search = self.request.GET.get('search')
        categorie = self.request.GET.get('categorie')

        if search:
            queryset = queryset.filter(
                Q(titre__icontains=search) |
                Q(contenu__icontains=search)
            )

        if categorie:
            queryset = queryset.filter(categorie__nom=categorie)

        return queryset.order_by('-date_entree')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Note.objects.select_related('categorie').values_list('categorie__nom', flat=True).distinct()
        return context


class NoteDetailView(LoginRequiredMixin,DetailView):  

    model = Note
    template_name = 'detail_note.html'
    context_object_name = 'details_note'


class NoteUpdateView(LoginRequiredMixin,UpdateView):  
    model = Note
    form_class = NoteForm
    template_name = 'modifier_note.html'  
    success_url = reverse_lazy('liste_notes')
    
class NoteDeleteView(LoginRequiredMixin ,DeleteView):
    model = Note
    template_name = 'supprimer_note.html'  
    success_url = reverse_lazy('liste_notes')

      
class MesNotesView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'mesnotes.html'
    context_object_name = 'mes_notes'

    def get_queryset(self):
        return Note.objects.filter(auteur=self.request.user)
