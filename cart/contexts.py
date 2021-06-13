from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.contrib import messages


currentDate = datetime.now()


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    discount = 0
    grand_total = 0
    subscription = False

    expiry = (currentDate + relativedelta(years=1)).date()
    cart = request.session.get("cart", {})
    consent = request.COOKIES.get("MMWconsent",)

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)

        # Only follow this step if subscription is still False
        if not subscription:
            if product.plan == 2:
                subscription = True

        total += quantity * product.price

        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total > 0:
        if subscription:
            add = float(total + (total * Decimal(settings.TAX_RATE)))
            grand_total = add * 0.9
            discount = add * 0.1
        else:
            grand_total = total + (total * Decimal(settings.TAX_RATE))

    tax = total * Decimal(settings.TAX_RATE)
    tax_rate = 100 * settings.TAX_RATE
    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "grand_total": grand_total,
        "subscription": subscription,
        "tax": tax,
        "tax_rate": tax_rate,
        "expiry": expiry,
        "discount": discount,
        "consent": consent,
    }

    return context
