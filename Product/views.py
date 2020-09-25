# gff
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from Product.models import Product
from cart.forms import CartAddProductForm


def Goods(request):
    Goods = Product.objects.all()
    return render(request, "../templates/Product/Product.html", {"Goods": Goods})


def create(request):
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.Description = request.POST.get("Description")
        if product.name == '':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        elif product.price == '':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        elif product.Description == '':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        else:
            product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "../templates/Product/create.html")


def edit(request, id):
    try:
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.name = request.POST.get("name")
            product.price = request.POST.get("price")
            product.Description = request.POST.get("Description")
            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "../templates/Product/edit.html", {"product": product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")


def product_detail(request, id):
    product = get_object_or_404(Product,
                                id=id,)
    cart_product_form = CartAddProductForm()
    return render(request, '../templates/cart/Product_detal.html', {'product': product,
                                                               'cart_product_form': cart_product_form})
