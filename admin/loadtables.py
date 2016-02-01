from google.appengine.ext import ndb
from datamodel.menuitem import MenuItem,MenuItemPrice
from datamodel.order import Order
from datamodel.user import User
from datamodel.article import Article

# Load MenuItems
class LoadDatabase:
    def __init__(self):
        pass

    def load_menuitems(self, dopurge=False):
        if dopurge:
            self.purge_entity(MenuItem())

        price1 = MenuItemPrice(unit_price=8.50,unit_type="individual")
        price_list = [price1]

        cuban_sandwich = MenuItem(is_available = True,
                                  is_vegetarian = False,
                                  unit_price = price_list,
                                  #unit_type = price_list,
                                  short_description = "Cuban Sandwich",
                                  long_description  = "Placeholder for Long Description"
                                  )
        cuban_sandwich.put()

        price1 = MenuItemPrice(unit_price=.85,unit_type="individual")
        price_list = [price1]

        croqueta_ham = MenuItem(is_available = True,
                                  is_vegetarian = False,
                                  unit_price = price_list,
                                  #unit_type = "individual",
                                  short_description = "Croqueta Ham",
                                  long_description =' Placeholder for Long Description'
                                  )
        croqueta_ham.put()

        price1 = MenuItemPrice(unit_price=5.00,unit_type="weight")
        price_list = [price1]
        frijolles = MenuItem(is_available = True,
                                  is_vegetarian = True,
                                  unit_price = price_list,
                                  #unit_type = "weight",
                                  short_description = "Frijolles Negros",
                                  long_description =' Placeholder for Long Description'
                                  )
        frijolles.put()

    def load_prices(self, dopurge = False):
        if dopurge:
            self.purge_entity(MenuItem())

    def load_articles(self, dopurge = False):
        if dopurge:
            self.purge_entity(Article())

    def load_orders(self, dopurge=False):
        if dopurge:
            self.purge_entity(Order())

    def purge_entity(self, entity):
        ndb.delete_multi(
            entity.query().fetch(keys_only=True)
        )

    def run(self, dopurge=False):
        self.load_menuitems(dopurge)
        #self.load_prices(dopurge)
        self.load_articles(dopurge)
        self.load_orders(dopurge)



