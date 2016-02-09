import os
import webapp2
import jinja2
from basehandler import BaseHandler

"""
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.join(os.path.dirname(__file__),"templates"),os.path.join(os.path.basename(__file__),"templates")]),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
"""

class MainHandler(BaseHandler):
    def get(self):
       template_values = {"company_name": "Favio's Mom","specialize_in": "All things Cuban Cusine, when you want it"}
       self.render_template("index.template", template_values)

    def __init__(self, *args, **kwargs):
        super(MainHandler, self).__init__(*args, **kwargs)