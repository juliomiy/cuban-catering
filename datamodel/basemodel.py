from google.appengine.ext import ndb

class BaseModel(ndb.Model):

    created = ndb.DateTimeProperty(required = True, auto_now_add = True)
    updated = ndb.DateTimeProperty(required = True, auto_now = True)
    updated_by = ndb.StringProperty(required = False)

    def get_all(self, entity):
        query = "select * from %s" % entity
        qry = ndb.gql(query)
        assert isinstance(qry, object)
        return qry