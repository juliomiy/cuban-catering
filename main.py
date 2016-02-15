#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
from webapp2_extras import routes
import jinja2
import logging
import logging.config
import ast


# temporary in main controller
from controller.testhandler import TestHandler
from controller.abouthandler import AboutHandler
from controller.contacthandler import ContactHandler
from controller.mainhandler import MainHandler
from controller.menuhandler import MenuHandler
from controller.orderhandler import OrderHandler
from controller.pricinghandler import PricingHandler
from controller.adminhandler import AdminHandler
from admin.loadtables import LoadDatabase
from controller.articlehandler import ArticleHandler
from controller.apihandler import APIHandler
# using the code as a scratch pad which I don't like but who will care

GOOGLEIDENTITYKEY = "AIzaSyCuZ6ZoiLR_3ObwVV8d667l4GSad3b4NLI"
'''
Of course will change this before going live
OAuth client
Here is your client ID
68222603480-7levoqto214hk8gprshg2rl1h300npso.apps.googleusercontent.com
Here is your client secret
PNxq831VpDrFx944A0oLf9A
'''


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def handle_404(request, response, exception):
    template_values = {}
    logging.exception(exception)
    template = JINJA_ENVIRONMENT.get_template('/templates/404.template')
    response.set_status(404)
    response.write(template.render(template_values))
    #response.write('Oops! I could swear this page was here!')

def handle_500(request, response, exception):
    template_values = {}
    logging.exception(exception)
    template = JINJA_ENVIRONMENT.get_template('/templates/500.template')
    response.set_status(404)
    response.write(template.render(template_values))

#logging.basicConfig(format='%(asctime)s %(message)s', filename='/logs/access.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')

try:
   with open('config/logger.dict') as f: config = ast.literal_eval(f.read())
   logging.config.dictConfig(config)
except Exception as ex:
   template = "An exception of type {0} occured. Arguments:\n{1!r}"
   message = template.format(type(ex).__name__, ex.args)
   print message

app = webapp2.WSGIApplication(
    [
        routes.DomainRoute('<api>.localhost', [
            webapp2.Route(r'/<version>/getcurrentlocation/', handler=APIHandler, handler_method='get_current_location', name='subdomain-home'),
        ]),
    ('/', MainHandler, "home"),
    ('/home', MainHandler, "home"),
    ('/menu', MenuHandler, "menu"),
    ('/contact', ContactHandler, "contact"),
    ('/order', OrderHandler, "order"),
    ('/pricing', PricingHandler, "pricing"),
    ('/about', AboutHandler, "about"),
    ('/test',  TestHandler, "test"),
    ('/admin', AdminHandler, "admin"),
    ('/admin/loaddatabase', LoadDatabase().run(True)),
    webapp2.Route(r'/article/<title>', handler=ArticleHandler, name='article'),
], debug=True)
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
