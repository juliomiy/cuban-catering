from google.appengine.ext import ndb
from datamodel.basemodel import BaseModel


class OrderItem(BaseModel):
    """ The individual MenuItem that is part of an order
    """
    quantity = ndb.IntegerProperty(required=True)
    price = ndb.FloatProperty(required=True)

class Order(BaseModel):
    """ An object for maintaining Order
    contains a repeatable Property for all of the MenuItems that are part of the order
    """
    order_items = ndb.StructuredProperty(OrderItem, repeated=True)
    pretax_price = ndb.FloatProperty(required=True)
    sales_tax = ndb.FloatProperty(required=True)
    total_price = ndb.FloatProperty(required=True)


