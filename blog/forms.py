from django import forms
from .models import Note


BASE_INPUT = "w-full px-4 py-2 border border-[#E2E2EA] rounded-xl bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[#2563EB] focus:border-[#2563EB] transition"


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['titre', 'image', 'contenu', 'categorie']

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': BASE_INPUT,
                'placeholder': 'Entrer le titre'
            }),

            'categorie': forms.Select(attrs={
                'class': BASE_INPUT
            }),

            'contenu': forms.Textarea(attrs={
                'class': BASE_INPUT + " h-32 resize-none",
                'placeholder': 'Décrire l’activité...'
            }),
        }