import os
import webapp2
import jinja2
from basehandler import BaseHandler
from datamodel.menuitem import MenuItem
"""
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.join(os.path.dirname(__file__),"templates"),os.path.join(os.path.basename(__file__),"templates")]),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
"""

class MenuHandler(BaseHandler):

    def get(self):
        template_values = {"menuitems" : {}}
        menuitem = MenuItem()
        items = menuitem.get_all_available()
        if items:
            template_values = {"menuitems" : items}

        self.render_template("menu.template", template_values)

    def __init__(self, *args, **kwargs):
        super(MenuHandler, self).__init__(*args, **kwargs)

