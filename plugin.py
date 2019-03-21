from time import time

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import supybot.schedule as schedule


class Greet(callbacks.Plugin):

    """
    This plugin greets users with a defined message when they join the
    channel. In order to use this plugin, supybot.plugins.Greet.enable
    must be True, and supybot.plugins.Greet.message must be set to the
    message you wish to send to users when they join.
    """

    _ignore = set([])

    def __init__(self, irc):
        self.__parent = super(Greet, self)
        self.__parent.__init__(irc)

    def _rememberNick(nick):
        if nick in self._ignore:
            self._ignore.remove()

    def _ignoreNick(self, irc, msg):
        channel = msg.args[0]

        if not self.registryValue('enable', channel):
            return

        delay = self.registryValue('grace', channel)

        if not msg.nick in self._ignore:
            self._ignore.add(msg.nick)
            schedule.addEvent(self._rememberNick, time() + delay,
                              args=(msg.nick,))

    def doJoin(self, irc, msg):
        channel = msg.args[0]

        if not self.registryValue('enable', channel):
            return

        greeting = self.registryValue('message', channel)
        delay = self.registryValue('grace', channel)

        if len(greeting.strip()) == 0:
            self.log.warn('Greeting empty for %s' % channel)
            return

        if (not ircutils.strEqual(msg.nick, irc.nick)
                and msg.nick not in self._ignore):
            self._ignore.add(msg.nick)
            irc = callbacks.SimpleProxy(irc, msg)
            irc.queueMsg(ircmsgs.privmsg(msg.nick, greeting))
            schedule.addEvent(self._rememberNick, time() + delay,
                              args=(msg.nick,))

    doPart = _ignoreNick
    doKick = _ignoreNick
    doQuit = _ignoreNick

Class = Greet
