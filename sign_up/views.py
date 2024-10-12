from django.shortcuts import render, redirect
from django.forms import ModelForm, PasswordInput
from sign_up.models import Etudiants
from django import forms
from django.contrib.auth.hashers import make_password

# Create your views here.

class EtudiantForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Etudiants
        fields = ['nom','prenom','email','password', 'photo']

def register(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            etudiant=form.save(commit=False)
            etudiant.password = form.cleaned_data['password']
            etudiant.save()
            return redirect('/success/')
    else:
        form = EtudiantForm()

    return render(request, 'register.html', {'form': form})





