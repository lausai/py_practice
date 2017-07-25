import os
import socket
import struct
import sys
import netifaces

def get_ip_address(ifname):
    for inf in netifaces.interfaces():
        if inf == ifname:
            if_info = netifaces.ifaddresses(inf)
            ip = if_info[2][0]["addr"]
            return ip

try:
    dut_nic = "{9ECA33E8-49AA-4386-8BFE-4D67DEF64863}"

    dut_if_ip = get_ip_address(dut_nic)
    print("IQ Interface IP: %s\n" % (dut_if_ip))

    ip = raw_input("Please input ip:\n")
    if ip == "":
        sys.exit()

    ip_arr = ip.split(".")

    for s in ip_arr:
        if not s.isdigit():
            raise Exception("Invalid IP")

        if int(s) > 255:
            raise Exception("Invalid IP")


    if len(ip_arr) != 2:
        raise Exception("Invalid IP")

    ip = "192.168.%s.%s" % (ip_arr[0], ip_arr[1])
    print("set IQ interface ip to %s" % (ip))

    cmd = "netsh interface ip set address name=\"IQ\" static %s 255.255.255.0" % (ip)
    os.system(cmd)

except Exception as e:
    print("Error: %s" % (e))

