from google.appengine.ext import ndb
from datamodel.menuitem import MenuItem,MenuItemPrice,MenuItemImage
from datamodel.order import Order
from datamodel.user import User
from datamodel.article import Article
from datamodel.contact import Contact

# Load MenuItems
class LoadDatabase:
    def __init__(self):
        pass

    def load_menuitems(self, dopurge=False):
        if dopurge:
            self.purge_entity(MenuItem())

        price1 = MenuItemPrice(unit_price=8.50,unit_type="individual")
        price_list = [price1]
        image_list = [MenuItemImage(filename="153805396_f489db1087_b.jpg")]

        cuban_sandwich = MenuItem(is_available = True,
                                  is_vegetarian = False,
                                  unit_price = price_list,
                                  #unit_type = price_list,
                                  short_description = "Cuban Sandwich",
                                  long_description  = "Placeholder for Long Description",
                                  name = "Cuban Sandwich",
                                  images = image_list
                                  )
        cuban_sandwich.put()

        price1 = MenuItemPrice(unit_price=.85,unit_type="individual")
        price_list = [price1]
        image_list = [MenuItemImage(filename="158958956_94d0de6e54_b.jpg")]

        croqueta_ham = MenuItem(is_available = True,
                                  is_vegetarian = False,
                                  unit_price = price_list,
                                  #unit_type = "individual",
                                  short_description = "Croqueta Ham",
                                  long_description =' Placeholder for Long Description',
                                  name = "Ham Croqueta",
                                  images = image_list
                                  )
        croqueta_ham.put()

        price1 = MenuItemPrice(unit_price=5.00,unit_type="weight")
        price_list = [price1]
        image_list = [MenuItemImage(filename="4536054891_ec15032bd7_o.jpg")]

        frijolles = MenuItem(is_available = True,
                                  is_vegetarian = True,
                                  unit_price = price_list,
                                  #unit_type = "weight",
                                  short_description = "Frijolles Negros",
                                  long_description =' Placeholder for Long Description',
                                  name = "Frijolles Negros",
                                  images = image_list
                                  )
        frijolles.put()

    def load_contact(self, dopurge = False):
        if dopurge:
            self.purge_entity(Contact())
        contact = Contact()
        contact.email = "support@faviosmom.com"
        contact.twitter = "faviosmom"
        contact.facebook = "faviosmom"
        contact.alexa = "Ask Favio's Mom"
        contact.phone = "212-555-1234"
        contact.put()

    def load_prices(self, dopurge = False):
        if dopurge:
            self.purge_entity(MenuItem())

    def load_articles(self, dopurge = False):
        if dopurge:
            self.purge_entity(Article())
        #About Page
        about_page = Article()
        about_page.title = "About Us"
        about_page.byline = "Favio's Mom"
        about_page.short_description = "About Us"
        about_page.body = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                             Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                             Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."""
        about_page.put()

    def load_orders(self, dopurge=False):
        if dopurge:
            self.purge_entity(Order())

    def purge_entity(self, entity):
        ndb.delete_multi(
            entity.query().fetch(keys_only=True)
        )

    def run(self, dopurge=False):
        self.load_menuitems(dopurge)
        self.load_contact()
        #self.load_prices(dopurge)
        self.load_articles(dopurge)
        #self.load_orders(dopurge)



