from .base import *


class Carts(CreateableApiResource, UpdateableApiResource, DeleteableApiResource):
    resource_name = 'carts'


class CartItems(CreateableApiSubResource, UpdateableApiSubResource, DeleteableApiSubResource):
    resource_name = 'items'
    parent_resource = 'carts'
    parent_key = 'cart_id'


class CartRedirectUrls(CreateableApiSubResource):
    resource_name = 'redirect_urls'
    parent_resource = 'carts'
    parent_key = 'cart_id'
