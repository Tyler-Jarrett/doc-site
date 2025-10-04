from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import models
from .forms import EntryForm

# Create your views here.
def main(request):
    return render(request, 'collection/main.html')

def success(request):
    msg = 'You have successfully added a new password'
    return render(request, 'collection/main.html', {"message": msg})

def submission(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')

    form = EntryForm()
    return render(request, "collection/submission.html", {"form": form})
