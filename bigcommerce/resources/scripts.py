from .base import *


class Scripts(ListableApiResource, CreateableApiResource,
              UpdateableApiResource, DeleteableApiResource):
    resource_name = 'content/scripts'
