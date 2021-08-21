# Import modules
from pypresence import Presence
import os

# Set client ID, mine is hidden for security
client_id = '<ID>'

# Set up Rich Presence
RPC = Presence(client_id, pipe=0)
RPC.connect()

# This function clears the console output
clear = lambda: os.system('cls')

# Main Code

# Clear everything on screen
clear()

# Print a text-based "GUI"
print("~~~~~~~Custom Discord Presence~~~~~~~     BETA 0.1")
print("     Developer: github/offsec64")
print(" ")
# Part for inputting the message you want (sets a variable)
msg = input("Input presence message, then press enter:")

# Once the user presses enter, clear the screen
clear()

# Print similar "GUI" but with info at the bottom
print("~~~~~~~Custom Discord Presence~~~~~~~     BETA 0.1")
print("     Developer: github/offsec64")
print(" ")
print("The message \"" + str(msg) + "\" will be on your discord status.")
print("You can minimize this window or close it to stop the status.")

# Push the Rich Presence info
while True:
    RPC.update(details=msg)
