# Trioyoyo
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/v/trioyoyo.svg" /></a>
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/l/trioyoyo.svg" /></a>
<a href="https://pypi.python.org/pypi/trioyoyo"><img src="https://img.shields.io/pypi/pyversions/trioyoyo.svg" /></a>
[![Build Status](https://travis-ci.org/henry232323/trioyoyo.svg?branch=master)](https://travis-ci.org/henry232323/trioyoyo)
<br />
A port of the Python IRC library oyoyo to trio for Python 3.5+
A Python trio IRC library

[See the documentation](http://typheus.me/trioyoyo)

Uses Trio instead of its original threading client. Creating an IRCClient instance will create the protocol instance.
To start the connection run `IRCClient.connect()` (coroutine)

Uses oyoyo from [illuminatedWax](https://github.com/illuminatedwax)'s [Pesterchum](https://github.com/illuminatedwax/pesterchum/tree/master/oyoyo), slightly modified

# Example
Examples can be found [here](https://github.com/henry232323/trioyoyo/tree/master/examples)
```python
from trioyoyo import IRCClient


class BasicExampleClient(IRCClient):
    async def connection_made(self):  # Overwrite connection_made to make it send join commands
        print("Successfully connected!")
        self.nick = "trioyoyo-example"
        await self.send("NICK", self.nick)
        await self.send("USER", self.nick, self.host, self.host, self.nick)
        await self.send("JOIN", "python")

    async def data_received(self, data):  # Print all data received
        print("Message Received: {}".format(data.decode()))

    async def connection_lost(self):  # Print on connection lost
        print("Connection has been lost!")


client = BasicExampleClient(address="irc.freenode.net", port=6667)
client.run()
```

