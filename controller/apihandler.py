import os
import webapp2
import jinja2
import json
import random
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

    def get_current_location(self,version,api,*args,**kwargs):
         location_dict = {}; payload = None
         #Germantown
         location_dict[0] = {"lat": 42.1342562,
                             "long":  -73.871242
                            }
         #hudson
         location_dict[1] = {"lat": 42.251476,
                             "long": -73.7862366
                            }
         #livingston
         location_dict[2] = {"lat": 42.1398114,
                            "long": -73.7870721
                           }
         maxkey = len(location_dict)
         if maxkey:
            index = random.randint(0,maxkey - 1)
            payload = location_dict[index]

         #if args is not None:
         self.request.GET.multi.items

         self.response.headers['Content-Type'] = 'application/json'
         obj = {
           'success': 'some var',
           'location': payload,
           'args' : self.request.route_args,
           'kwargs': self.request.route_kwargs,

         }
         self.response.headers.add_header("Access-Control-Allow-Origin", "*")
         self.response.out.write(json.dumps(obj))

    def __init__(self, *args, **kwargs):
        super(APIHandler, self).__init__(*args, **kwargs)