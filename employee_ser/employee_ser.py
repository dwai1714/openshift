from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
#import bcrypt
from eve import Eve
#from eve.auth import BasicAuth
#from flask import current_app as app
import logging
#import os
#from flask import Flask, request, redirect, url_for
#from flask import Response

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Employee Service Started")



app = Eve()

# from eve.auth import requires_auth
# from datetime import timedelta
# from flask import make_response, request, current_app
# from functools import update_wrapper


http_server = HTTPServer(WSGIContainer(app))
#http_server.listen(9001)
http_server.listen(8080)
IOLoop.instance().start()
