from flask import abort


def abort_if_doesnt_exist(*objs, message=None, code=400):
    not_existing = []
    for i, o in enumerate(objs):
        if not o and o != 0:
            not_existing.append(i)

    if len(not_existing) > 0:
        message = str(message) + " - " + str(not_existing)
        abort(code, message)
