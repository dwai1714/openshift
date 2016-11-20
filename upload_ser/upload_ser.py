from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import logging
import os
from flask import Flask, request, redirect, url_for, jsonify
from flask import Response



logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("uppload Service Started")



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

    try:
        return Response("health OK", status=200, mimetype='application/json')
    except:
       return Response("health Not OK", status=400, mimetype='application/json')

@app.route('/api/v1/fileupload', methods=['POST'])
@crossdomain(origin='*')

def fileupload():
    try:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                raise ValueError("No File")
            file = request.files['file']
            file.save(os.path.join('/tmp/', file.filename))
            resp = Response(file.filename, status=200, mimetype='application/json')
            print "resp is ", resp
            return resp
    except ValueError as e:
        print "e is " , e
        resp = Response(e, status=400, mimetype='application/json')
        return resp

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(9009)
IOLoop.instance().start()

# curl -H "Content-Type: multipart/form-data" \
#-H "Accept: application/json" \
#-H "Expect:" \
#-F file=@/users/dwai1714/Desktop/Payslip.pdf \
#-X POST http://localhost:9009/api/v1/fileupload