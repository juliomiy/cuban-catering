import os
import webapp2
import jinja2
from basehandler import BaseHandler
from datamodel.article import Article


class ArticleHandler(BaseHandler):
    def get(self):
       template_values = {}
       self.render_template("article.template", template_values)

    def get(self, title):
        """
        The title parameter is returned in uri encoded form which needs to be converted to non encoded fashion for lookup in Article Table
        :param title: uri encoded string
        :return: article template
        """
        template_values = {}; decoded_title = title
        article = Article()

        if None is not title:
            decoded_title = article.normalize_string_to_uri(title,False)
        response = article.get_article_by_title(decoded_title)

        if None is not response and isinstance(response,dict):
            template_values["article"] = response

        self.render_template("article.template", template_values)

    def __init__(self, *args, **kwargs):
        super(ArticleHandler, self).__init__(*args, **kwargs)

