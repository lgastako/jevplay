# jevplay

My playground for experimenting with JEV and similar things (so far just Laya).

The two main things right now are jgrep and lgrep which are both semantic grep
implemented with jev and laya respectively.

For lgrep I use lserve to load the model once and keep it in memory and then
talk to it with lclient so it's fast.

lclient and lserve just expose laya via zmq.

