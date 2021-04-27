from django.http import HttpResponse


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
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook
        """
        return HttpResponse(
            content=f'Intent Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle payment_intent.failed webhook
        """
        return HttpResponse(
            content=f'Intent Webhook received: {event["type"]}',
            status=200)
