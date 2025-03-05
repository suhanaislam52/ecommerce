# core/management/commands/simulate_webhook.py
from django.core.management.base import BaseCommand
import json
import requests

class Command(BaseCommand):
    help = 'Simulate Stripe webhook events'

    def add_arguments(self, parser):
        parser.add_argument('event_type', type=str)

    def handle(self, *args, **kwargs):
        event_type = kwargs['event_type']
        url = 'http://localhost:8000/stripe/webhook/'  # Your webhook endpoint

        # Simulate a Stripe event payload
        payload = {
            'id': 'evt_test_webhook',
            'object': 'event',
            'type': event_type,
            'data': {
                'object': {
                    'id': 'pi_test_payment_intent'
                }
            }
        }

        response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        print(f'Webhook sent with status: {response.status_code}')
        print('Response body:', response.text)
