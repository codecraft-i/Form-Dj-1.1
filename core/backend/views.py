from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UsersForm

def home(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successfully')
    else:
        form = UsersForm()

    return render(request, 'index.html', {'form': form})

def success_view(request):

    return render(request, 'successfully.html')