from django.shortcuts import render, redirect

# Create your views here.
def success_view(request):
    if request.method == 'POST':
        return redirect('/login/')
    return  render(request, 'success.html')