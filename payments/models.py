from django.db import models

from django.db import models
from django.conf import settings
import conekta
import json
# Create your models here.

class Sale(models.Model):
	def __init__(self, *args, **kwargs):
		super(Sale, self).__init__(*args, **kwargs)

		conekta.api_key = settings.CONEKTA_PRIVATE_KEY

		conekta.api_version = "2.0.0"

	def charge(self, price_in_cents, token_id):
		try:
			order = conekta.Order.create({
				"line_items": [{
					"name": "Tacos",
					"unit_price": 1000,
					"quantity": 12
				}],
				"shipping_lines": [{
					"amount": 1500,
					"carrier": "FEDEX"
				}], #shipping_lines - physical goods only
				"currency": "MXN",
				"customer_info": {
					"customer_id": "cus_2fkJPFjQKABcmiZWz"
				},
				"shipping_contact":{
					"address": {
						"street1": "Calle 123, int 2",
						"postal_code": "06100",
						"country": "MX"
					} #shipping_contact - required only for physical goods
				},
				"metadata": { "description": "Compra de creditos: 300(MXN)", "reference": "1334523452345" },
				"charges":[{
					"payment_method": {
					"type": "default"
				}  #payment_method - use the customer's <code>default</code> - a card
			  }]
			})
		except conekta.ConektaError as e:
			print (e.message)
