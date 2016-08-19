import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs


class Greet(callbacks.Plugin):
    """
    This plugin greets users with a defined message when they join the
    channel. In order to use this plugin, supybot.plugins.Greet.enable
    must be True, and supybot.plugins.Greet.message must be set to the
    message you wish to send to users when they join.
    """

    def __init__(self, irc):
        self.__parent = super(Greet, self)
        self.__parent.__init__(irc)

    def doJoin(self, irc, msg):
        channel = msg.args[0]

        if not self.registryValue('enable', channel):
            return

        greeting = self.registryValue('message', channel)

        if len(greeting.strip()) == 0:
            self.log.warn('Greeting empty for %s' % channel)
            return

        if not ircutils.strEqual(msg.nick, irc.nick):
            irc = callbacks.SimpleProxy(irc, msg)
            irc.queueMsg(ircmsgs.privmsg(msg.nick, greeting))

Class = Greet
