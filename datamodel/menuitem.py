from google.appengine.ext import ndb

from datamodel.basemodel import BaseModel

selection = ['individual', 'weight', 'small_portion', "large_portion"]

class MenuItemPrice(BaseModel):
    """ The price records for the differentportion types

    """
    unit_price = ndb.FloatProperty(required=True)
    unit_type = ndb.StringProperty(choices=selection, required=True)
    unit_size = ndb.IntegerProperty(required=False)

class MenuItem(BaseModel):
    """     The menu Items for the business

    Each of the entries will define an object of  what we have available for sale.
    The only thing that can be ordered will be what is in the table and what is currently available as defined in the
    available property.
    Can align with Google App Engine BigTable Eventual consistency as these objects won't change frequently.
    """
    long_description = ndb.StringProperty(required = True, indexed = False)
    short_description = ndb.StringProperty(required = True, indexed = False)
    is_available = ndb.BooleanProperty(required = True, indexed = False)
    is_vegetarian = ndb.BooleanProperty(required = True, indexed = False)
    url_article = ndb.StringProperty(required = False, indexed = False)
    calories = ndb.IntegerProperty(required = False)
    #unit_price = ndb.FloatProperty(required = True)
    #unit_type = ndb.StringProperty(choices=selection, required=True)
    unit_price = ndb.StructuredProperty(MenuItemPrice, repeated=True)


    def get__(self):
        """
        return: get all elements in the MenuItem table.
        """
        pass


