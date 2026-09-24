import sys
import json

import zmq


def encode(state, questions):
    return json.dumps([state, questions])


def decode(reply):
    return json.loads(reply)


def remote(state, questions):
    address = "tcp://localhost:5555" # TODO args
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.setsockopt(zmq.CONNECT_TIMEOUT, 1000)
    socket.connect(address)
    req = encode(state, questions)
    socket.send_string(req)
    reply = socket.recv_string()
    resp = decode(reply)
    return resp
