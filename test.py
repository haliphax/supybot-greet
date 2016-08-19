from supybot.test import *

class GreetTestCase(PluginTestCase):
    plugins = ('Greet',)

    def testGreet(self):
        self.assertNotError('greet')
