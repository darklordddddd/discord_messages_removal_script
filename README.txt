This script removes all of your messages in a Discord channel. Optionally can clear an entire channel, this is for admins or moderators only.

In order for this to work, you need to obtain the identifiers and an authorization token.

Enable a developer mode in the Discord settings and open a notepad program.
Right click on a preferred channel and copy ID, then paste it into the notepad. Do the same with your profile located in the "Member List".

Now that you got all IDs, you need an authorization token.
Press Ctrl+Shift+I to open a developer console, select "Network" tab, then select XHR tab under the toolbar. Press F5 to refresh info.
Select "messages" node, then select "Headers" tab, look for an "authorization" key, copy it into the notepad as well.

Launch a script and paste the requested information from a notepad.

Dependencies:
1. Python 3
2. "Requests" module for Python 3