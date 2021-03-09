# importiamo forms in modo da poter creare una classe figlia e utilizzarne le funzioni
# https://docs.djangoproject.com/en/3.0/topics/forms/#the-django-form-class

# Documentazione sui campi utilizzabili con Form e Parametri: 
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/

from django import forms
class FormContatto(forms.Form):
     nome = forms.CharField()
     cognome = forms.CharField()
     email = forms.EmailField()
     contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area Testuale! Scrivi pure!"}))
