#!/usr/bin/env python

# Copyright 2016 Google Inc.
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

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import subprocess               # For running shell commands
import socket

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
RW_DIR = "/tmp/"                # Other directories are write protected!
RESPONSE_FILE_NAME = "serverData.csv"


# We set a parent key on the 'Greetings' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate should be limited to
# ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity.

    We use guestbook_name as the key.
    """
    return ndb.Key('Guestbook', guestbook_name)


# [START greeting]
class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END greeting]


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        page = "login.html"
        requestResultsText = "Nothing to see here"

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            page = "WWW/index.html"
            #requestResultsText = subprocess.check_output(["java FrontEndClient", "get office stats"])
            #requestResultsText = subprocess.check_output("uname -a", stderr=subprocess.STDOUT, shell=True)
            #requestResultsText = run(["java", "FrontEndClient"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #requestResultsText = os.system("uname -a")
            #            requestResultsText = os.system("java /tmp/FrontEndClient catsh")
            #requestResultsText = os.system("java /tmp/FrontEndClient catsh")
            # requestResultsText = subprocess.Popen(["java", "/tmp/FrontEndClient", "catsh"],
            #                                       stdout=subprocess.PIPE,
            #                                       stderr=subprocess.STDOUT)
            #os.system("java /tmp/FrontEndClient catsh")
            #open(RW_DIR + RESPONSE_FILE_NAME, "w").write("This is secret")
            #requestResultsText = open(RW_DIR + "FrontEndClient", "r").read()
            requestResultsText = self.requestResults()
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            page = "WWW/login.html"

        template_values = {
            'user': user,
            'greetings': greetings,
            'guestbook_name': urllib.quote_plus(guestbook_name),
            'url': url,
            'url_linktext': url_linktext,
            'requestResultsText': requestResultsText,
        }

        template = JINJA_ENVIRONMENT.get_template(page)
        self.response.write(template.render(template_values))

    def requestResults(self):
        HOST = "ec2-52-90-192-10.compute-1.amazonaws.com"
        PORT_NUM = 8192

        client_socket = socket.socket()
        client_socket.connect((HOST, PORT_NUM))

        message = "Get data"

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        client_socket.close()
        return data
#         HOST = "ec2-52-90-192-10.compute-1.amazonaws.com"
#         PORT = 8192

#         client_socket = socket.socket()
#         client_socket.connect((HOST, PORT))

#         message = "cats"

# #        while message.lower().strip() != 'bye':
# 	client_socket.send(message.encode())
# 	ret = client_socket.recv(1024)
#         client_socket.close()
#         return ret
# [END main_page]


# [START guestbook]
class Guestbook(webapp2.RequestHandler):

    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = Author(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())

        greeting.content = self.request.get('content')
        greeting.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))
# [END guestbook]


# This code is taken from the following thread: https://stackoverflow.com/questions/40590192/getting-an-error-attributeerror-module-object-has-no-attribute-run-while
def run(*popenargs, **kwargs):
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)
    try:
        stdout, stderr = process.communicate(input)
    except:
        process.kill()
        process.wait()
        raise
    retcode = process.poll()
    if check and retcode:
        raise subprocess.CalledProcessError(
            retcode, process.args, output=stdout, stderr=stderr)
    return retcode, stdout, stderr


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)
# [END app]
