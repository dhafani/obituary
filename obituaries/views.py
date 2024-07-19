
from django.shortcuts import render, redirect
from .models import Obituary
from django.http import HttpResponse

from django.http import HttpResponse

def submit_obituary(request):
    if request.method != 'POST':
        return render(request, 'obituary_form.html')
    
    name = request.POST.get('name')
    date_of_birth = request.POST.get('date_of_birth')
    date_of_death = request.POST.get('date_of_death')
    content = request.POST.get('content')
    author = request.POST.get('author')
    
    if not all([name, date_of_birth, date_of_death, content, author]):
        return HttpResponse("Please fill in all fields.")
    
    obituary = Obituary(name=name, date_of_birth=date_of_birth, date_of_death=date_of_death, content=content, author=author)
    obituary.save()
    
    return HttpResponse("Obituary submitted successfully!")


# obituaries/views.py
def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})



