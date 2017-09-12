from trioyoyo import CommandHandler, protected, CommandClient


class CommandExampleClient(CommandClient):
    nick = "trioyoyo-example"


class ExampleCommandHandler(CommandHandler):
    first = False
    async def notice(self, client, *args):  # Will be called on the NOTICE command
        if not self.first:
            await client.send("NICK", client.nick)
            await client.send("USER", client.nick, client.host, client.host, client.nick)
            await client.send("JOIN", "python")
            self.first = True
            
        print("Notice received: {}".format(b" ".join(args).decode()))

    async def endofmotd(self, client, *args):  # Called on numeric command 376 endofmotd
        print("We've reached the end of the MOTD!")

    @protected
    def protected_operation(self):
        # Can't be called by a command, protected
        print(self.client.nick)


if __name__ == "__main__":
    client = CommandExampleClient(ExampleCommandHandler, host="irc.freenode.net", port=6667)
    client.run()

# We can run the connect coroutine directly instead of using the blocking run
# await client.connect()

