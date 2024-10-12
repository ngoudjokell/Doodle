from django.shortcuts import render, redirect
from django.forms import ModelForm
from myform.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=('name','firstname','email','message')
    
def contact(request):
    if request.method == 'POST':
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('success')
    else:
        contact_form=ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})


# Create your views here.
