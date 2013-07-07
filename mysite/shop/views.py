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
def add_to_basket(request, product_id = 'product_id'):
    if Product.objects.filter(id=product_id).exists():
        if 'product_id' in request.session:
            request.session.get('product_id').append(product_id)
            request.session.modified = True
        else:
            request.session['product_id'] = [product_id]
    return HttpResponseRedirect('/products/')