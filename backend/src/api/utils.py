import os
from functools import wraps
from flask import abort, request, jsonify

def authentification_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            abort(401, "No token provided")
        if token != os.environ.get('AUTH_TOKEN'):
            abort(401, "Invalid token")
        return f(*args, **kwargs)
    return inner

def abort_if_doesnt_exist(*objs, message=None, code=400):
    not_existing = []
    for i, o in enumerate(objs):
        if not o and o != 0:
            not_existing.append(i)

    if len(not_existing) > 0:
        message = str(message) + " - " + str(not_existing)
        abort(code, message)
