#gff
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from Product.models import Product




def Goods(request):
    Goods = Product.objects.all()
    return render(request, "Product/index.html", {"Goods": Goods})


def create(request):
    if request.method == "POST":
        Product1 = Product()
        Product1.name = request.POST.get("name")
        Product1.price = request.POST.get("price")
        Product1.Description = request.POST.get("Description")
        if Product1.name =='':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        elif Product1.price == '':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        elif Product1.Description == '':
            return HttpResponseNotFound("<h2>Не все поля заполнены!!!</h2>")
        else:
            Product1.save()
        return HttpResponseRedirect("/")

def edit(request, id):
    try:
        Product1 = Product.objects.get(id=id)

        if request.method == "POST":
            Product1.name = request.POST.get("name")
            Product1.price = request.POST.get("price")
            Product1.Description = request.POST.get("Description")
            Product1.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "Product/edit.html", {"Product1": Product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")


def delete(request, id):
    try:
        Product1 = Product.objects.get(id=id)
        Product1.delete()
        return HttpResponseRedirect("/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Товар не найден</h2>")
