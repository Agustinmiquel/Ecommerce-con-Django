import uuid
import decimal
from django.db import models

from users.models import User
from Tienda_online.models import Product
from django.db.models.signals import m2m_changed

from django.db.models.signals import pre_save

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product) #Muchos a muchos
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    FEE = 0.05

    def __str__(self):
        return self.cart_id
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()

        if self.order:
            self.order.update_total()

    @property
    def order(self):
        return self.order_set.first()

    def update_subtotal(self):
        self.subtotal = sum([product.price for product in self.products.all()])
        self.save()
    
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id= str(uuid.uuid4())
    
def update_totals(sender, instance, action,*args, **kwargs ):
    if action == 'post_add' or action =='post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_cart_id, sender=Cart)
m2m_changed.connect(update_totals, sender=Cart.products.through)