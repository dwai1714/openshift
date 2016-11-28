from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from flask import current_app as app
import logging
import os
from flask import Flask, request, redirect, url_for
from flask import Response


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("email_ser started")

app = Flask(__name__)

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/status', methods=['GET'])
@crossdomain(origin='*')
def health():
    from flask import request, jsonify
    import socket
    hostname = socket.gethostname()

    try:
        return Response("health OK "+ hostname, status=200, mimetype='application/json')
    except:
       return Response("health Not OK", status=400, mimetype='application/json')


@app.route('/api/v1/email', methods=['POST'])
@crossdomain(origin='*')

def send_email():

    from flask import request, jsonify
    import send_mail
    content = request.json
    try:
        fromaddr = content["fromaddr"]
        toadd = content["toadd"]
        password = content["password"]
    except:
        resp = Response("From Address, To Address and Password are Required", status=400, mimetype='application/json')
        return resp
    subject = content.get("subject" , "No Subject")
    filename = content.get("filename", 0)
    dir = content.get("dir", 0)
    body = content.get("body" , " ")

    try:
        if (send_mail.send_gmail_message(toadd, fromaddr,password, subject, dir, filename, body)) == False:
            resp = Response("Attachment Missing", status=400, mimetype='application/json')
        else:
            resp = Response("Mail Sent", status=200, mimetype='application/json')
        return resp
    except :
        resp = Response("Error Processing Mail", status=400, mimetype='application/json')
        return resp


http_server = HTTPServer(WSGIContainer(app))
http_server.listen(9008)
#http_server.listen(8080)
IOLoop.instance().start()

# {
# 	"toadd":["dwaip.chowdhury@accionlabs.com", "dwaip@yahoo.com"],
# 	"subject":"Sent from email Service",
# 	"body" : "Lets see if this works",
# 	"dir":"/tmjp/",
# 	"filename":"1.pdf"
# }
#curl -H "Content-Type: application/json" -X POST -d '{"toadd":["dwaip.chowdhury@accionlabs.com", "dwaip@yahoo.com"], "subject":"Sent from email Service", "body" : "Lets see if this works"}' http://restful-restful.44fs.preview.openshiftapps.com/api/v1/email
