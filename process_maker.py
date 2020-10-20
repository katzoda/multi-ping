#!/usr/bin/env python3

file_dev = "devices.txt"

f_dev = open(file_dev, 'r')

i = 1

#following code creates scripts that are run by multiping.py
for ip in f_dev.readlines():
    ip = ip.strip()
    with open("template_ping_v2.txt") as file_templ:
        for line in file_templ.readlines():
            ping_process = open("ping_process" + str(i) + ".py", "a")
            if "import" in line: #allows us to add a new lines below the 'import subprocess' statement in the ping process script
                ping_process.write(line + "\n")
                ping_process.write("ip_add = " + "'" + ip + "'" + "\n")
                ping_process.write("p = " + str(i) + "\n") # used in print(f"Process {p} is running....")
            else:
                ping_process.write(line + "\n")
    i += 1

f_dev.close()
