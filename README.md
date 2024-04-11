# Rick Roller v2: A Simple DND Bot
Welcome to my humble repository. This is a bot I made using Python 3 for rolling dice in DND campaigns.
## Commands
`/roll` - Rolls a dice with the specified number of sides

`/multi_roll` -  Rolls multiple of the same dice specified 

`/custom_roll` - Up to three (3) multi_rolls at once, allowing for multiple types of dice

`/wrangler_protocol` - Wrangles a specified user - *Requires special permission to execute*

-------- **BEWARE**: This **WILL** result in spam --------

To make things easier, this was built with tree commands to prompt the user and make things easier
## Setup Notes
You will need to replace the `API_Token.example` and `Wrangler_Protocol_Users.example` files with `.txt` files.

Make sure to keep the same file names; just change the extension.

### API_Token.txt
Simply throw your Discord app API token in here. No quotes required; just raw text.

### Wrangler_Protocol_Users.txt
Throw the users you want to give wrangling access to in here. You will need to toss their Discord ID in here. Raw text; no quotes.

This functionality is intended based on my use case. It could be tied into a role, but you will not have admin on every server. Sometimes, you don't want to get wrangled, and I'm greedy with power.

## Final Notes
Have fun with this! Every once in a while (probably once a year), I will take a look at this again to update code with something I see fit. Depends if I have the time to play DND anymore.
