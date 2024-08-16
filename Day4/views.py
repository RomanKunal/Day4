from django.shortcuts import render
from . import forms

def home(request):
    form = forms.InputForm()
    return render(request, 'index.html', {'form': form})


