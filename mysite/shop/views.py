from django.http import HttpResponse
from shop.forms import ApplicationForm
from django.shortcuts import render
import datetime

def apply_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.applied_date = datetime.datetime.now()
            instance.save()
            return HttpResponse('Saved to database')
        else:
            form = ApplicationForm()
            return render(request, 'shop/application_form.html', {'form': form})
    else:
        form = ApplicationForm()
        return render(request, 'shop/application_form.html', {'form': form})