# -*- coding: utf-8 -*-


MONGO_URI = "mongodb://dwaipayan:dwaip123@ds119738.mlab.com:19738/openshift"



# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20
X_DOMAINS = '*'
X_HEADERS = ['Authorization','Content-type']
URL_PREFIX = 'api'
API_VERSION = 'v1'
STATUS = 'success'
STATUS_OK = 'true'
STATUS_ERR = 'false'

employee = {
    # 'title' tag used in item links.
    'item_title': 'Employee Roster',

    'additional_lookup': {
        'url': 'regex("(.*?)")',
        'field': 'SSO'
    },

    'schema': {
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
        },
        'SSO': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
            'required': True,
            'unique': True,
        } ,
        'email': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required': True,
             'unique': True,
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        'startdate': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 15,
        },
        # An embedded 'strongly-typed' dictionary.
    }
}


status = {
    # 'title' tag used in item links.
    'item_title': 'status',

    'additional_lookup': {
        'url': 'regex("(.*?)")',
        'field': 'success'
    },

    'schema': {
        'success': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
        }
    }
}


DOMAIN = {
    'employee': employee,
    'status': status
}
