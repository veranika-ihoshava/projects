from django.db import models
from django.forms import ModelForm

class User(models.Model):
    name = models.CharField(max_length = 200)
    login = models.EmailField('E-mail', max_length = 200, blank = True)
    password = models.CharField(max_length = 20)

    def __unicode__(self):
        return self.name
	
class Product_group(models.Model):
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200, blank = True)
    
    def __unicode__(self):
        return self.name
	
class Product(models.Model):
    serial_number = models.IntegerField()
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200, blank = True)
    price = models.DecimalField(max_digits=20, decimal_places=5)
    count = models.IntegerField()
    group = models.ForeignKey(Product_group)
    image = models.ImageField(upload_to='images', blank=True)
    def show_image(self):
        if self.image:
            return '<img src="%s" width="120" height="120" alt="Product image">' % self.image.url
        else:
            return '<img src="/static/images/default.jpg" width="120" height="120" alt="Image not found">'
    show_image.allow_tags = True

    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.serial_number, self.name, self.price, self.count, self.group)
	
class Order(models.Model):
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Product)
    def __unicode__(self):
        return unicode(self.user)

class Application(models.Model):
    username = models.CharField(max_length = 100, blank=True)
    surname = models.CharField(max_length = 100, blank=True)
    login = models.EmailField('E-mail', max_length = 100)
    applied_date = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField()
