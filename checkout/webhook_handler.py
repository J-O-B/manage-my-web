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

        grand_total = round(intent.charges.data[0].amount_captured / 100, 2)
        # correct till here

        # Ensure correct data type is captured
        for field, value in billing_details.items():
            if value == "":
                billing_details[field] = None
        print(billing_details)
        order_exists = False
        order = Order.objects.get(
            full_name__iexact=billing_details['name'],
            email__iexact=billing_details['email'],
            phone_number__iexact=billing_details['phone'],
            country__iexact=billing_details.address['country'],
            postcode__iexact=billing_details.address['postal_code'],
            town_or_city__iexact=billing_details.address['city'],
            street_address1__iexact=billing_details.address['line1'],
            street_address2__iexact=billing_details.address['line2'],
            grand_total=grand_total,
            subscription=subscription,
            subscriber=subscriber,
            date=datetime.now(),
            order_number=pid,
        )
        print(order)

        return HttpResponse(
            content=f'Intent Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.failed webhook
        """
        return HttpResponse(
            content=f'Intent Webhook Received: {event["type"]}',
            status=200)
