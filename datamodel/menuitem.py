from google.appengine.ext import ndb

from datamodel.basemodel import BaseModel

selection = ['individual', 'weight', 'small_portion', "large_portion"]

class MenuItemImage(BaseModel):
    filename = ndb.StringProperty(required = False, indexed = False)

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
    name = ndb.StringProperty(required = True, indexed = True)
    long_description = ndb.StringProperty(required = True, indexed = False)
    short_description = ndb.StringProperty(required = True, indexed = False)
    is_available = ndb.BooleanProperty(required = True, indexed = True)
    is_vegetarian = ndb.BooleanProperty(required = True, indexed = False)
    url_article = ndb.StringProperty(required = False, indexed = False)
    calories = ndb.IntegerProperty(required = False)
    #unit_price = ndb.FloatProperty(required = True)
    #unit_type = ndb.StringProperty(choices=selection, required=True)
    unit_price = ndb.StructuredProperty(MenuItemPrice, repeated=True)
    images = ndb.StructuredProperty(MenuItemImage, repeated=True)

    def get__(self):
        """
        return: get all elements in the MenuItem table.
        """
        pass

    def get_all_available(self):
        """
        get all menu items that are currently available - this will filter by the is_available property
        :return:
        """
        resp_dict = {}

        qry = MenuItem.query(MenuItem.is_available == True)
        for item in qry:
            is_available = True
            is_vegetarian = item.is_vegetarian
            long_description = item.long_description
            short_description = item.short_description
            calories = item.calories
            url_article = item.url_article
            dict = {"name":  "test",
                    "is_available" : is_available,
                    "is_vegetarian": is_vegetarian,
                    "long_description": long_description,
                    "short_description": short_description
                    }
            resp_dict[item.key] = dict
        return resp_dict


