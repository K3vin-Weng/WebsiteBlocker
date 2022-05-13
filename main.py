# This program blocks, unblocks and lists blocked websites
#   NOTE!!! : this program must be run as administrator to work

import blocking
#######################################################################################################################

print("Press Q to quit the program at anytime.\n")

while (True):
    cmd = input("B (Block), U (Unblock) or L (List)?\n")

    if (cmd == "Q") or ():
        print("You have quit.")
        break
    elif cmd == "U":
        website = input("Which website do you wish to block?\n")
        if website == "Q":
            print("You have quit.")
            break
        blocking.unblock(website)
        Warning = "{} has been unblocked! Confirm that it is the correct website!\nElse make sure to rectify the error.\n"
        print(Warning.format(website))
    elif cmd == "B":
        website = input("Which website do you wish to block?\n")
        if website == "Q":
            print("You have quit.")
            break
        blocking.block(website)
        Warning = "{} has been blocked! Confirm that it is the correct website!\nElse make sure to rectify the error.\n"
        print(Warning.format(website))
    else:
        print("Sorry the command you have inputted is unavailable, please try again.")

