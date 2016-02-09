import os
import webapp2
import jinja2
from basehandler import BaseHandler
from datamodel.contact import Contact

"""
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.join(os.path.dirname(__file__),"templates"),os.path.join(os.path.basename(__file__),"templates")]),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
"""

class ContactHandler(BaseHandler):
    def get(self):

       template_values = {}
       contact = Contact()
       response = contact.get_contact()
       template_values = {"contact": response}
       self.render_template("contact.template", template_values)

    def __init__(self, *args, **kwargs):
        super(ContactHandler, self).__init__(*args, **kwargs)

