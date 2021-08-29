from flask import abort

def abort_if_doesnt_exist(*objs, message=None):
    for o in objs:
        if not o:
            abort(400, message)