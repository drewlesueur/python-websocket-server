def ws_send(socko, message):
    socko.send('\x00' + message.encode('utf-8') + '\xff')