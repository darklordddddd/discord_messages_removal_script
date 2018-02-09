This script removes all of your messages in a Discord channel. Optionally can clear an entire channel, this is for admins or moderators only.

In order for this to work, you need to obtain the identifiers and an authorization token.

Enable a developer mode in the Discord settings and open a notepad program.
Right click on a preferred channel and copy ID, then paste it into the notepad. Do the same with your profile located in the "Member List".

Now that you got all IDs, you need an authorization token.
Press Ctrl+Shift+I to open a developer console, select "Application" tab. Open "Local Storage" node, select "https://discordapp.com".
Look for a token key and copy its value (without quotes) into the notepad.

Launch a script and paste the requested information from a notepad.

Dependencies:
1. Python 3
2. "Requests" module for Python 3