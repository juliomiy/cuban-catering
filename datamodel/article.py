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
    body = short_description = ndb.TextProperty(required=True, indexed=False)
    byline = ndb.StringProperty(required=True, indexed=True)



