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

def show_all_nic():
    for inf in netifaces.interfaces():
        try:
            if_info = netifaces.ifaddresses(inf)
            print("nic: %s, ip: %s" % (inf, if_info[2][0]["addr"]));
        except:
            pass

try:
    dut_nic = "{CB4B3F5C-7FB9-4282-B06D-107ED7DCF73F}"

    dut_if_ip = get_ip_address(dut_nic)
    print("DUT Interface IP: %s\n" % (dut_if_ip))

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
    print("set DUT interface ip to %s" % (ip))

    cmd = "netsh interface ip set address name=\"DUT\" static %s 255.255.255.0" % (ip)
    os.system(cmd)

except Exception as e:
    print("Error: %s" % (e))
