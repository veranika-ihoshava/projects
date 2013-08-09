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
def add_to_basket(request, product_id):
    product_id = int(product_id)
    if Product.objects.filter(id=product_id).exists():
        print '1. exists in DB = ' + str(product_id)
        if 'products_in_basket' in request.session:
            print '2. session exists'
            if request.session.get('products_in_basket').has_key(product_id): #if this product already exists in the session
                print '3. product_id exists in session'
                products_in_basket = request.session.get('products_in_basket')
                count = products_in_basket[product_id]
                products_in_basket[product_id] = count + 1
                request.session.modified = True
                print request.session.get('products_in_basket')
            else:
                print '3. add product to session = ' + str(product_id)
                request.session.get('products_in_basket')[product_id] = 1
                request.session.modified = True
                print 'session: '
                print request.session.get('products_in_basket')
        else:
            request.session['products_in_basket'] = {}
            request.session['products_in_basket'][product_id] = 1
    return HttpResponseRedirect('/products/')


@require_GET
def delete_from_basket(request, product_id='product_id'):
    if Product.objects.filter(id=product_id).exists():
        if 'product_id' in request.session:
            request.session.get('product_id').remove(product_id)
            request.session.modified = True
    return HttpResponseRedirect('/basket/')


def session_products(request, session_products='products_in_basket'):
    if session_products in request.session:
        product_id_list = request.session.get(session_products).keys()
        product_count_list = request.session.get(session_products).values()
        print product_count_list
        product_list = list(Product.objects.filter(id__in=product_id_list).values('id', 'name', 'price', 'image', 'description'))

        return render(request, 'shop/product_list_basket.html', {'product_list': product_list})
    else:
        return render(request, 'shop/product_list_basket.html',
                      {'product_list': []})

