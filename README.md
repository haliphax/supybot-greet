# supybot Greet plugin

This plugin will send a privmsg to users when joining a channel where it is
enabled and a greeting message has been set. It is simple in that it does
not consider netsplits or known users; it just sends the message for every
join.

## settings

- `supybot.plugins.Greet.enable` _(Boolean)_: Whether or not the plugin is
  active on the selected channel (default: `False`)
- `supybot.plugins.Greet.message` _(String)_: The message to send to users when
  they join the selected channel
- `supybot.plugins.Greet.grace` _(PositiveInteger)_: Grace period (in seconds)
  to avoid re-greeting someone after a kick, part, or join (default: `30`)

To set these, use the `config channel` command.
