from django.db import models

#class Poll(models.Model):
#    question = models.CharField(max_length = 200)
#    pub_date = models.DateTimeField('date published')
#class Choice (models.Model):
#    poll = models.ForeignKey (Poll)
#    choice = models.CharField(max_length = 200)
#    votes = models.IntegerField()
# Create your models here.

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
    
    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.serial_number, self.name, self.price, self.count, self.group)
	
class Order(models.Model):
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Product)
    def __unicode__(self):
        return unicode(self.user)