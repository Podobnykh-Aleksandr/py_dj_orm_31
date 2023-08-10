from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    up_down = False
    if 'max' in sort:
        up_down = True
    if 'release_date' in sort:
        sort = 'release_date'
    elif 'price' in sort:
        sort = 'price'
    elif 'name' in sort:
        sort = 'name'
    else:
        sort.Contains('id')
    template = 'catalog.html'
    phones_objects = Phone.objects.order_by(sort)
    if up_down:
        phones_objects = phones_objects.reverse()
    context = {'phones': phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    context = {'phone': phone_object[0]}
    return render(request, template, context)
