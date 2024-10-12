
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import Login
from sign_up.models import Etudiants
from django.contrib import messages
from django.contrib.auth.hashers import check_password


# Create your views here.
class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields=['email','password']


def connecter(request):
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            try:
                etudiant = Etudiants.objects.get(email=email)
                if etudiant.password==password:
                    return redirect('/admin/')
                else:
                    messages.error(request, "Mot de passe incorrect")
            except Etudiants.DoesNotExist:
                messages.error(request, "email non trouvé")
    else:
        form=LoginForm()
    return render(request, 'login.html', {'form': form}) 
