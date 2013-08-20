import datetime
from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.decorators.http import require_GET
from django.views.generic.edit import FormView
from forms import ApplicationForm
from models import Product, News

class ApplicationView(FormView):
    template_name = 'shop/application_form.html'
    form_class = ApplicationForm
    success_url = '/products/'

    def form_valid(self, form):
        form.save()
        send_mail('I miss you!', 'I miss you!', 'alesha@dev.by', [form.cleaned_data['login']], fail_silently=True)
        return super(ApplicationView, self).form_valid(form)


class NewsListView(ListView):   #override object manager
    def get_queryset(self):
        date_time_now = datetime.datetime.now()
        return News.objects.filter(publication_start_at__lte=date_time_now, publication_end_at__gte=date_time_now)

class NewsDetailView(DetailView):
    def get_queryset(self):
        date_time_now = datetime.datetime.now()
        return News.objects.filter(publication_start_at__lte=date_time_now, publication_end_at__gte=date_time_now)


@require_GET
def add_to_basket(request, product_id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
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
    return HttpResponseRedirect('/basket/')


def session_products(request):
    if 'products_in_basket' in request.session:
        products_in_basket_ids = request.session.get('products_in_basket').keys()
        product_list = list(Product.objects.filter(id__in=products_in_basket_ids).values('id', 'name', 'price', 'image', 'description'))
        return render(request, 'shop/product_list_basket.html', {'product_list': product_list})
    else:
        return render(request, 'shop/product_list_basket.html',
                      {'product_list': []})
