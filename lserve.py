import json
import sys

import laya
import zmq

from laya import Router


def decode(msg):
    return json.loads(msg)


def encode(resp):
    return json.dumps(resp)


def main():
    print("Preloading router...")
    router = Router(preload=True)
    print("Router loaded.")

    address = "tcp://*:5555" # TODO args
    context = zmq.Context()
    socket = context.socket(zmq.REP) # TODO
    socket.bind(address)

    print("Listening at ", address)

    while True:
        msg = socket.recv_string()
        print("Received: ", msg)

        state, questions = decode(msg)
        resp = router.predict(state, questions)
        reply = encode(resp)

        socket.send_string(reply)


if __name__ == "__main__":
    main()
