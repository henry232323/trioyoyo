from trioyoyo import IRCClient


class BasicExampleClient(IRCClient):
    async def connection_made(self):  # Overwrite connection_made to make it send join commands
        print("Successfully connected!")
        self.nick = "trioyoyo-example"
        await self.send("NICK", self.nick)
        await self.send("USER", self.nick, self.address, self.address, self.nick)
        await self.send("JOIN", "python")

    async def data_received(self, data):  # Print all data received
        print("Message Received: {}".format(data.decode()))

    async def connection_lost(self):  # Print on connection lost
        print("Connection has been lost!")

if __name__ == "__main__":
    client = BasicExampleClient(host="irc.freenode.net", port=6667)
    client.run()
