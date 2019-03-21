import supybot.conf as conf
import supybot.registry as registry


def configure(advanced):
    conf.registerPlugin('Greet', True)


Greet = conf.registerPlugin('Greet')
conf.registerChannelValue(
    Greet,
    'enable',
    registry.Boolean(False, """Determines whether or not the bot will send the
                            configured greeting (defined by
                            supybot.plugins.Greet.message) when someone joins
                            the channel."""))
conf.registerChannelValue(
    Greet,
    'message',
    registry.String('', """The greeting that is sent to someone when they join
                        the channel."""))
conf.registerChannelValue(
    Greet,
    'grace',
    registry.PositiveInteger(30, """The length of the grace period (in seconds)
                                 for not re-greeting someone after a kick,
                                 join, or part event."""))
