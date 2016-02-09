import os
import webapp2
import jinja2
from basehandler import BaseHandler
from datamodel.article import Article

"""
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader([os.path.join(os.path.dirname(__file__),"templates"),os.path.join(os.path.basename(__file__),"templates")]),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
"""

class AboutHandler(BaseHandler):
    def get(self):
       """ Simply retrieves an Article entity from the database keyed by the Title
       assumption is there is a 1:1 correspondence between the page and 1 article entity
       :return:
       """
       article = Article()
       response = article.get_article_by_title("About Us")
       template_values = {"article": response}
       self.render_template("about.template", template_values)

    def __init__(self, *args, **kwargs):
        super(AboutHandler, self).__init__(*args, **kwargs)