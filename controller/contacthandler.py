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

class AboutHandler(BaseHandler):
    def get(self):
       template_values = {}
       self.render_template("about.template", template_values)

    def __init__(self, *args, **kwargs):
        super(AboutHandler, self).__init__(*args, **kwargs)