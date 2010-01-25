import util

def handle(data, socko, to_read, to_write, to_error,scope):
    util.ws_send(socko, scope.setdefault('last_message', ""))
    scope['last_message'] = data