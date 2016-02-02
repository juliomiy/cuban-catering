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

class TestHandler(BaseHandler):

    def get(self):
        template_values = {}
        #template = JINJA_ENVIRONMENT.get_template('test.template')
        self.render_template('test.template', template_values)
        #self.response.write(template.render(template_values))
