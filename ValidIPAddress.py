#Clear Console
import os
from re import X
def clear_console():
    os.system('cls')
clear_console()

def validIPAddress():
    queryIP = input('Enter an IP Address: ')
    def IPv4_check():
        # Set up for logic
        ip_int = []
        IPv4 = True
        ip = queryIP.split('.')
        # Checks if the ip address only contains integers
        try:
            for i in ip:
                ip_int.append(int(i))
        except:
            IPv4 = False
        # Checks if the ip address has only 4 sections
        if len(ip) != 4:
            IPv4 = False
        # Checks if each of the numbers of the ip address are between 0 and 255
        for i in range(len(ip_int)):    
            if ip_int[i] > 0 or ip_int[i]< 255:
                IPv4 = False
        # Checks if the leading number in any part of the ip address is a zero
        for i in ip:
            if len(i) >= 2 and i[0] == '0':
                IPv4 = False
    IPv4_check()

validIPAddress()


