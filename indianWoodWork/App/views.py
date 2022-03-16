from django.shortcuts import render, HttpResponse
from .models import ImageSlide, Product, ContactUs
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    imageslide = ImageSlide.objects.all()
    param = {'data': imageslide}
    return render(request, 'index.html', param)


def product(request, slug):
    products = Product.objects.filter(product_cat=slug)
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    param = {'data': page_obj}
    return render(request, 'products.html', param)


def productcategory(request):
    Almiras = Product.objects.filter(product_cat='Almiras').order_by('update')[::-1]
    LCDPanels = Product.objects.filter(product_cat='LCD Panels').order_by('update')[::-1]
    ModularKitchens = Product.objects.filter(product_cat='Modular Kitchens').order_by('update')[::-1]
    Beds = Product.objects.filter(product_cat='Beds').order_by('update')[::-1]
    Tables = Product.objects.filter(product_cat='Tables').order_by('update')[::-1]
    ShowroomWorks = Product.objects.filter(product_cat='Showroom Works').order_by('update')[::-1]
    Doors = Product.objects.filter(product_cat="Doors").order_by('update')[::-1]
    Palles = Product.objects.filter(product_cat='Palles').order_by('update')[::-1]

    param = {'Almiras': Almiras[:3], 'LCDPanels': LCDPanels[:3], 'ModularKitchens': ModularKitchens[:3],
             'Beds': Beds[:3],
             'Tables': Tables[:3], 'ShowroomWorks': ShowroomWorks[:3], 'Doors': Doors[:3], 'Palles': Palles[:3]}
    return render(request, 'productcategory.html', param)


def search(request):
    if request.method == 'GET':
        searchtext = request.GET.get('searchtext')
        if len(searchtext) < 2 or len(searchtext) > 20:
            messages.error(request, " Search Text is too Small/Too Greater")
            products = {}
        else:
            products = Product.objects.filter(name__icontains=searchtext)
            if len(products) < 1:
                messages.error(request, " No Product is Found ! ")
            else:
                messages.success(request, " Search is Success ")
    param = {'data': products}
    return render(request, 'products.html', param)


def productview(request, slug):
    products = Product.objects.get(slug=slug)
    param = {'data': products}
    return render(request, 'productview.html', param)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('content')
        if len(name) > 2 and len(email) > 5 and len(phone) > 9 and len(comment) != 0:
            contact = ContactUs(name=name, email=email, phone=phone, comment=comment)
            contact.save()
            messages.success(request, " Your Details is Successfuly Save")
        else:
            messages.error(request, " Please Fill the Right Details")
    return render(request, 'contact.html')
