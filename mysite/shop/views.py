from forms import ApplicationForm
from django.http import HttpResponse
from django.shortcuts import render


def apply_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved to database')
    else:
        form = ApplicationForm()
    return render(request, 'shop/application_form.html', {'form': form})