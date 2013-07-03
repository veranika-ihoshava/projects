from django.http import HttpResponse
from forms import ApplicationForm
from django.shortcuts import render
import datetime

def apply_form(request):
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid() and request.POST['checked']:
            form.save()
            return HttpResponse('Saved to database')
    return render(request, 'shop/application_form.html', {'form': form})