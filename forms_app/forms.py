from django import forms
from .models import Contatto
from django.core.exceptions import ValidationError

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"

    
    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viole le norme del sito!")
        return dati