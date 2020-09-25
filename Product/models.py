from django.db import models
from django.shortcuts import render
from django.urls import reverse
from cart.forms import CartAddProductForm

class Product(models.Model):

    name = models.CharField(max_length=20)
    price = models.IntegerField()
    Description = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        index_together = (('id'),)

    def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('OnlineStore:product_detail',
                        args=[self.id, self.slug])


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})