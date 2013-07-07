from forms import ApplicationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from models import Product
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

def add_to_basket(request):
    if request.method == 'GET':
        if request.GET.get('product_id'):
            new_product_id = request.GET.get('product_id')
            if Product.objects.filter(id=new_product_id).exists():
                if request.session.get('product_id'):
                    request.session.get('product_id').append(new_product_id)
                    request.session.modified = True
                    return HttpResponseRedirect('/products/')
                request.session['product_id'] = [new_product_id]
                return HttpResponseRedirect('/products/')
    return HttpResponse('Cheeeaateeeeer!')