from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.db.models.functions import Lower
from datetime import datetime


def all_products(request):
    products = Product.objects.all()
    all_categories = Category.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    custom_title = None
    subtitle = None

    # update ratings
    for product in products:
        if product.rating_count > 0:
            now = datetime.now()

            # Only refresh ratings max once per day
            if product.rating_update:
                if product.rating_update.date() != now.date():
                    total = product.rating_total
                    count = product.rating_count
                    product.rating = total / count
                    product.rating_update = now
                    product.save()
                else:
                    pass
            # If there is no rating, then no update
            else:
                pass

    if request.GET:
        if 'on_sale' in request.GET:
            products = products.filter(on_sale=2)
            custom_title = "Products On Sale"

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            subtitle = sort
            if sortkey == 'name':
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == "category":
                sortkey = "category__name"

            if 'direction' in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if "webdesign" in categories:
                custom_title = "All Web Design Products"
            elif "seo" in categories:
                custom_title = "All SEO Products"
            else:
                category = Category.objects.filter(name=categories[0])
                for c in category:
                    custom_title = c.friendly_name
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You Didn't Enter Any Search Criteria.")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(description__icontains=query))
            products = products.filter(queries)
            custom_title = "Search Results For " + query

    current_sorting = f'{sort}_{direction}'

    found = products.count()
    found_str = f'Displaying {found} Items'
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'categories': all_categories,
        'current_sorting': current_sorting,
        'custom_title': custom_title,
        'subtitle': subtitle,
        'found_str': found_str,
    }
    return render(request, template, context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    rating = None
    whole_stars = None
    half_star = None
    if product.rating_count > 0:
        total = product.rating_total
        count = product.rating_count
        rating = total / count

        whole_stars = range(int(rating))
        if rating % 1 != 0:
            half_star = 1

    if product.image5:
        carousel = [
            product.image1.url,
            product.image2.url,
            product.image3.url,
            product.image4.url,
            product.image5.url,
        ]
    elif product.image4:
        carousel = [
            product.image1.url,
            product.image2.url,
            product.image3.url,
            product.image4.url,
        ]
    elif product.image3:
        carousel = [
            product.image1.url,
            product.image2.url,
            product.image3.url,
        ]
    elif product.image2:
        carousel = [
            product.image1.url,
            product.image2.url,
        ]
    else:
        carousel = False

    saving = None

    if product.normal_price:
        saving = (
            product.normal_price - product.price) / product.normal_price * 100

    template = 'products/product_detail.html'
    context = {
        'product': product,
        'saving': saving,
        'rating': rating,
        'whole_stars': whole_stars,
        'half_star': half_star,
        'carousel': carousel,
    }
    return render(request, template, context)
