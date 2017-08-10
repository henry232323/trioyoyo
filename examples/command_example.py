from trioyoyo.client import CommandClient
from trioyoyo.cmdhandler import CommandHandler, protected


class CommandExampleClient(CommandClient):
    def __init__(self, *args, **kwargs):
        CommandClient.__init__(self, *args, **kwargs)
        self.nick = "trioyoyo-example"
                
    async def connection_made(self):  # Overwrite connection_made to make it send join commands
        print("Successfully connected!")
        await self.send("NICK", self.nick)
        await self.send("USER", self.nick, self.address, self.address, self.nick)
        await self.send("JOIN", "python")


class ExampleCommandHandler(CommandHandler):
    async def notice(self, client, *args):  # Will be called on the NOTICE command
        print("Notice received: {}".format(b" ".join(args).decode()))

    async def endofmotd(self, client, *args):  # Called on numeric command 376 endofmotd
        print("We've reached the end of the MOTD!")

    @protected
    def protected_operation(self):
        # Can't be called by a command, protected
        print(self.client.nick)


client = CommandExampleClient(CommandHandler, address="irc.freenode.net", port=6667)
client.run()

# We can run the connect coroutine directly instead of using the blocking run
# await client.connect()

