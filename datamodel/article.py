from google.appengine.ext import ndb
from datamodel.basemodel import BaseModel


class Article(BaseModel):
    """ An object for Articles which by convention will regardly be a
    1:1 mapping with the MenuItems but may just be general purpose artilce like in the
    about us form. No need for a sophisticated CMS given the few number of article like
    content on this site.
    The title field will be used as part of the URI so it will have to be unique
    """
    title = ndb.StringProperty(required=True, indexed=True)
    short_description = ndb.StringProperty(required=True, indexed=False)
    body = ndb.TextProperty(required=True, indexed=False)
    byline = ndb.StringProperty(required=True, indexed=True)
    article_key = ndb.StringProperty(required=False, indexed=True)


    def get_article_by_title(self,title):
        """
        :param title of article
        :return: dictionary of values for use by template
        """
        resp_dict = {}; response = None
        qry = Article.query(Article.title == title)

        for item in qry:
            """ title is usually stored as a free text which is not optimal for a uri
            call normalize method to replace various characters , predominantly space to
            valid uri character
            """
            article_uri = self.normalize_string_to_uri(item.title,True)
            response = { "title": item.title,
                         "short_description": item.short_description,
                         "body": item.body,
                         "byLine": item.byline,
                         "article_key": item.key,
                         "article_uri": article_uri
                        }

        if response is not None and isinstance(response,dict):
            resp_dict = response
        return resp_dict

