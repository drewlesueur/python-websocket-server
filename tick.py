import util
def tick(socko,scope):
    util.ws_send(socko, scope.setdefault("last_message", ""))