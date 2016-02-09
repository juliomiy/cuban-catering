from google.appengine.ext import ndb
from datamodel.basemodel import BaseModel


class Contact(BaseModel):
    """ basic Contact information. Very simple at the outset, only one record necessary
    """
    facebook = ndb.StringProperty(required=False, indexed=False)
    twitter = ndb.StringProperty(required=False, indexed=False)
    email = ndb.StringProperty(required=False, indexed=False)
    phone = ndb.StringProperty(required=False, indexed=False)
    alexa = ndb.StringProperty(required=False, indexed=False)

    def get_contact(self):
        resp_dict = {}; response = None
        qry = self.get_all("Contact")

        for item in qry:
            response = { "facebook": item.facebook,
                         "twitter": item.twitter,
                         "email": item.email,
                         "phone": item.phone,
                         "alexa": item.alexa
                        }
        resp_dict  = response
