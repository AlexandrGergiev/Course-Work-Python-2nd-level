from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product, Brand
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})


def about(request):
    return render(request, "myshop/about.html")


class BrandListView(generic.ListView):
    model = Brand
    context_object_name = "brand_list"
    queryset = Brand.objects.all()
    template_name = "brand/list.html"
