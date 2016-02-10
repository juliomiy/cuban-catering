import os
import webapp2
import jinja2
from basehandler import BaseHandler
from datamodel.article import Article

class APIHandler(BaseHandler):
    def get(self):
       """ Simply retrieves an Article entity from the database keyed by the Title
       assumption is there is a 1:1 correspondence between the page and 1 article entity
       :return:
       """
       template_values = {}
       self.render_template("api.template", template_values)

    def get(self, version, api):
        self.get()

    def __init__(self, *args, **kwargs):
        super(APIHandler, self).__init__(*args, **kwargs)