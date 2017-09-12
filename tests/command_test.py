import unittest
import random

import trio

from trioyoyo import CommandHandler, CommandClient


class CommandTestClient(CommandClient):
    nick = "trioyoyo" + "".join(random.sample("1234567890", 4))

    async def connect(self):
        with trio.move_on_after(120):
            await CommandClient.connect(self)


class TestCommandHandler(CommandHandler):
    first = False
    welc = False

    async def notice(self, client, *args):  # Will be called on the NOTICE command
        if not self.first:
            await client.send("NICK", client.nick)
            await client.send("USER", client.nick, client.host, client.host, client.nick)
            await client.send("JOIN", "python")
            self.first = True

        print("Notice received: {}".format(b" ".join(args).decode()))

    async def welcome(self, client, *args):  # Called if we successfully login
        print(b" ".join(args).decode())
        self.welc = True
        self.client.close()


class CommandTest(unittest.TestCase):
    def test_command(self):
        client = CommandTestClient(TestCommandHandler, host="irc.freenode.net", port=6667)
        client.run()

        self.assertTrue(client.command_handler.first)
        self.assertTrue(client.command_handler.welc)


if __name__ == "__main__":
    unittest.main()
