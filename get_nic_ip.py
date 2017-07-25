import os
import socket
import struct
import sys
import netifaces
import _winreg as wr


for inf in netifaces.interfaces():
    if_info = netifaces.ifaddresses(inf)

    if 2 in if_info:
        ip = if_info[2][0]["addr"]
        print("%s %s" % (inf, ip))
