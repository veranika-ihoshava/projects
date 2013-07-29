from forms import ApplicationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from models import Product
from django.shortcuts import render
from django.views.decorators.http import require_GET


def apply_form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved to database')
    else:
        form = ApplicationForm()
    return render(request, 'shop/application_form.html', {'form': form})


@require_GET
def add_to_basket(request, product_id='product_id'):
    if Product.objects.filter(id=product_id).exists(): #what for this???
        if 'product_id' in request.session:
            request.session.get('product_id').append(product_id)
            request.session.modified = True
        else:
            request.session['product_id'] = [product_id]
    return HttpResponseRedirect('/products/')

@require_GET
def delete_from_basket(request, product_id='product_id'):
    if Product.objects.filter(id=product_id).exists():
        if 'product_id' in request.session:
            request.session.get('product_id').remove(product_id)
            request.session.modified = True
    return HttpResponseRedirect('/basket/')


def session_products(request, product_id='product_id'):
    if product_id in request.session:
        product_id_list = request.session.get(product_id)
        Product.objects.filter(id__in=product_id_list)
        return render(request, 'shop/product_list_basket.html',
                  {'product_list': Product.objects.filter(id__in=product_id_list)})
    else:
        return render(request, 'shop/product_list_basket.html',
                      {'product_list': []})

