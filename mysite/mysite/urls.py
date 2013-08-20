from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from django.views.generic import ListView
from shop.models import Product, Product_group
from shop.views import add_to_basket, delete_from_basket, delete_all_from_basket, session_products
from shop.views import ApplicationView, NewsListView, NewsDetailView

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^products/$', ListView.as_view(model=Product)),
    (r'^groups/$', ListView.as_view(
        queryset=Product_group.objects.order_by('name'),
        context_object_name='groups'
    )),
    url(r'^apply/$', ApplicationView.as_view()),
    url(r'^products/(?P<product_id>\d{1,4})/add/$', add_to_basket),
    url(r'^products/(?P<product_id>\d{1,4})/delete/$', delete_from_basket),
    url(r'^products/all/delete/$', delete_all_from_basket),
    url(r'^basket/$', session_products),
    url(r'^news/$', NewsListView.as_view()),
    url(r'^news/(?P<slug>\w{1,100})$', NewsDetailView.as_view()),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout)
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
