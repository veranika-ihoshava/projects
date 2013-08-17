from forms import ApplicationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from models import Product, Application
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic.edit import FormView


class ApplicationView(FormView):
    template_name = 'shop/application_form.html'
    form_class = ApplicationForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        return super(ApplicationView, self).form_valid(form)

#def apply_form(request):
#    if request.method == 'POST':
#        form = ApplicationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponse('Saved to database')
#    else:
#        form = ApplicationForm()
#    return render(request, 'shop/application_form.html', {'form': form})


@require_GET
def add_to_basket(request, product_id):
    product_id = int(product_id)
    if Product.objects.filter(id=product_id).exists():
        if 'products_in_basket' in request.session:
            products_in_basket = request.session.get('products_in_basket')
            if product_id in products_in_basket.keys():
                products_in_basket[product_id] += 1
                request.session.modified = True
            else:
                products_in_basket[product_id] = 1
                request.session.modified = True
        else:
            request.session['products_in_basket'] = {product_id : 1}
    return HttpResponseRedirect('/products/')


@require_GET
def delete_from_basket(request, product_id='product_id'):
    product_id=int(product_id)
    if Product.objects.filter(id=product_id).exists() and 'products_in_basket' in request.session:
        products_in_basket = request.session.get('products_in_basket')
        if product_id in products_in_basket.keys():
            if products_in_basket[product_id] == 1:
                del products_in_basket[product_id]
            else:
                products_in_basket[product_id] -= 1
            request.session.modified = True
    return HttpResponseRedirect('/basket/')


@require_GET
def delete_all_from_basket(request):
    if 'products_in_basket' in request.session:
        del request.session['products_in_basket']
#            request.session.modified = True
    return HttpResponseRedirect('/basket/')


def session_products(request):
    if 'products_in_basket' in request.session:
        products_in_basket_ids = request.session.get('products_in_basket').keys()
        product_list = list(Product.objects.filter(id__in=products_in_basket_ids).values('id', 'name', 'price', 'image', 'description'))
        return render(request, 'shop/product_list_basket.html', {'product_list': product_list})
    else:
        return render(request, 'shop/product_list_basket.html',
                      {'product_list': []})

