# Trioyoyo
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/v/trioyoyo.svg" /></a>
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/l/trioyoyo.svg" /></a>
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/pyversions/trioyoyo.svg" /></a>
<br />
A port of the Python IRC library oyoyo to trio for Python 3.5+
A Python trio IRC library

Uses Trio instead of its original threading client. Creating an IRCClient instance will create the protocol instance.
To start the connection run `IRCClient.connect()` (coroutine)

Uses oyoyo from [illuminatedWax](https://github.com/illuminatedwax)'s [Pesterchum](https://github.com/illuminatedwax/pesterchum/tree/master/oyoyo), slightly modified
