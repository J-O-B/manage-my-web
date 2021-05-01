from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from datetime import datetime

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """
    Class to handle various stripe webhooks
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic, unknown or unexpected webhook events
        """
        return HttpResponse(
            content=f'Unhandled Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        subscription = intent.metadata.subscription
        if subscription == "true":
            subscriber = "Yes"
        else:
            subscriber = "No"

        billing_details = intent.charges.data[0].billing_details

        # Personal Data:
        full_name = billing_details.name
        email = billing_details.email
        phone_number = billing_details.phone

        # Address:
        country = billing_details.address.country
        town_or_city = billing_details.address.city
        street_address1 = billing_details.address.line1
        street_address2 = billing_details.address.line2
        postcode = billing_details.address.postal_code


        grand_total = round(intent.charges.data[0].amount_captured / 100, 2)
        # correct till here
   
        if full_name == "":
            full_name = None
        if email == "":
            email = None
        if phone_number == "":
            phone_number = None
        if country == "":
            country = None
        if town_or_city == "":
            town_or_city = None
        if street_address1 == "":
            street_address1 = None
        if street_address2 == "":
            street_address2 = None
        if postcode == "":
            postcode = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=full_name,
                    email__iexact=email,
                    phone_number__iexact=phone_number,
                    stripe_pid=pid
                )

                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook Received: {event["type"]} | SUCCESS: Verified order already exists',
                status=200)
        else:
            order = None
            try:
                for id, data in json.loads(cart).items():
                    product = Product.objects.get(id=id)
                    if product.plan == 2:
                        subscription = True
                        subscriber = "Yes"
                        break
                    else:
                        subscription = False
                        subscriber = "No"
                order = Order.objects.create(
                    full_name=full_name,
                    email=email,
                    phone_number=phone_number,
                    country=country,
                    postcode=postcode,
                    town_or_city=town_or_city,
                    street_address1=street_address1,
                    street_address2=street_address2,
                    stripe_pid=pid,
                    original_cart=cart,
                    date=datetime.now(),
                    subscriber=subscriber,
                    subscription=subscription,
                    tax=settings.TAX_RATE,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if product.plan == 2:
                        subscription = True
                    else:
                        subscription = False
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            subscription=subscription,
                        )
                        order_line_item.save()
                    else:
                        for quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                subscription=subscription,
                            )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook Received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Intent Webhook Received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.failed webhook
        """
        return HttpResponse(
            content=f'Intent Webhook Received: {event["type"]}',
            status=200)
