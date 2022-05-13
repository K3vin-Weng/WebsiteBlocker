# the blocking module provides functions to block and unblock websites
#   through the host file on Windows (C:\Windows\System32\Drivers\etc\hosts)
import os
import shutil


# num of lines in the original host file (you may want to change this if the number does not match)
num_og_lines = 26
# local host ip
local_host = "127.0.0.1"
# hosts_path file path for Windows
hosts_path = "C:\Windows\System32\Drivers\etc\hosts"
########################################################################################################################

def block(site):
    block_line = local_host + "     " + site + "\n"
    hosts = open(hosts_path, "r")
    for i in range(1, num_og_lines):
        hosts.readline()

    line = hosts.readline()
    blocked = False
    while line != "":
        if block_line == line:
            print("Already Blocked!\n")
            blocked = True
            break
        line = hosts.readline()

    hosts.close()
    if not(blocked):
        hosts = open(hosts_path, "a")
        hosts.write(block_line + "\n")



def unblock(site):
    rm_line = local_host + "     " + site + "\n"
    hosts = open(hosts_path, "r")
    temp_f = open("temp", "a")

    for i in range(1, num_og_lines):
        line = hosts.readline()
        temp_f.write(line)

    in_list = False
    line = hosts.readline()
    while line != "":
        if rm_line == line:
            in_list = True
        elif "\n" != line:
            line = line + "\n"
            temp_f.write(line)
        line = hosts.readline()
    hosts.close()
    temp_f.close()

    shutil.copyfile("temp", hosts_path)
    os.remove("temp")
    if not(in_list):
        text = "{} was not previously blocked. No changes has been made!"
        print(text.format(site))

