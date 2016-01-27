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
import jinja2

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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('index.template')
        self.response.write(template.render(template_values))
        #self.response.write('Hello world!')

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('contact.template')
        self.response.write(template.render(template_values))

class MenuHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('menu.template')
        self.response.write(template.render(template_values))

class OrderHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('order.template')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home', MainHandler),
    ('/menu', MenuHandler),
    ('/contact', ContactHandler),
    ('/order', OrderHandler),
], debug=True)
