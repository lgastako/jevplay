# jevplay

My playground for experimenting with JEV and similar things (so far just Laya).

The two main things right now are `jgrep.py` and `lgrep.py` which are both
semantic grep implemented with jev and laya respectively.

For `lgrep.py` I use `lserve.py` to load the model once and keep it in memory
and then talk to it with `lclient.py` so it's fast.

`lserve.py` just exposes laya via zmq and then `lclient.py` accesses it.

I use `uv` for everything, so eg `uv run lgrep.py ...` or `uv run jgrep.py ...`
