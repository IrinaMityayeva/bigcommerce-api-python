from __future__ import print_function
import bigcommerce_v3.api

api = bigcommerce_v3.api.BigcommerceApi(client_id='id', store_hash='hash', access_token='token')

print(repr(api.Time.all()))
