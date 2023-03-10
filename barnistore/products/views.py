from django.shortcuts import render

from products.models import Products, Category

# products = Products.objects.all()[10] это значит, что мы хотим взять все объекты из
# базы Product и вывести первые 10 объектов


def index(request):
    """Main page"""
    products = Products.objects.all()[:10]
    return render(request, 'products/index.html',
    {'products': products},
    )


def product(request, slug):
    """Product page"""
    product = Products.objects.get(slug=slug)
    return render(request, 'products/product.html',
    {'product': product},
    )


def category(request, slug):
    """Category page"""
    category = Category.objects.get(slug=slug)
    return render(request, 'products/category.html',
    {'category': category},
    )


def create(request):
    """Product create"""
    context = {}
    return render(request, 'products/product_create.html', context,
    )