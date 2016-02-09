from google.appengine.ext import ndb
import logging

class BaseModel(ndb.Model):

    created = ndb.DateTimeProperty(required = True, auto_now_add = True)
    updated = ndb.DateTimeProperty(required = True, auto_now = True)
    updated_by = ndb.StringProperty(required = False)

    def get_all(self, entity):
        query = "select * from %s" % entity
        logging.debug(query)
        qry = ndb.gql(query)
        assert isinstance(qry, object)
        return qry

    def normalize_string_to_uri(self,uri,encode = True):
        if encode and uri:
            normalized_uri = uri.replace(" ","_")
        elif not encode and uri:
            normalized_uri = uri.replace("_"," ")
        return normalized_uri
