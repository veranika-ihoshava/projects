from forms import ApplicationForm
from django.http import HttpResponse
from django.shortcuts import render
from models import Product


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
                    return HttpResponse('Products in your basket: ' + str(request.session.get('product_id')))
                request.session['product_id'] = [new_product_id]
                return HttpResponse('First product added to basket: ' + str(request.session.get('product_id')))
    return HttpResponse('Cheeeaateeeeer!')