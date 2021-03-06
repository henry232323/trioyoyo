#!/usr/bin/python3
# Copyright (c) 2016-2017, henry232323
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
"""A small, simple irc lib for python suitable for bots, clients and anything else.

For more information and documentation about the original package:
   http://code.google.com/p/oyoyo/

For documentation on trioyoyo: http://trioyoyo.typheus.me/
"""
from .helpers import HelperClient
from .client import IRCClient, CommandClient
from .cmdhandler import protected, CommandHandler, DefaultCommandHandler, DefaultBotCommandHandler, BotCommandHandler

from . import _oyoyo
from ._oyoyo.parse import parse_nick, parse_raw_irc_command
from ._oyoyo.ircevents import all_events, generated_events, protocol_events, numeric_events
from ._oyoyo.cmdhandler import CommandError, NoSuchCommandError, ProtectedCommandError, IRCClientError
