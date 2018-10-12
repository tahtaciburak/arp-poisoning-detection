import os
import time
import re

def is_arp_spoofed():
    os.system('arp -a > .arp_dump')
    mac_list = []
    with open(".arp_dump","r") as f:
        for line in f.readlines():
            mac_addr = re.search(r'([0-9A-Fa-f]{1,2}[:-]){5}([0-9A-Fa-f]{1,2})', line, re.I).group()
            if mac_addr not in mac_list:
                mac_list.append(mac_addr)
            else:
                return True
    os.system('rm .arp_dump')
    return False


def main():
    if(is_arp_spoofed()):
        print("ARP Poisoning Detected")
    else:
        print("ARP looks fine")

if __name__ == '__main__':
    main()
