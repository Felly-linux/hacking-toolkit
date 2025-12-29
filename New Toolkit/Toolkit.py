import pyfiglet 
import os
from colorama import Fore, Back, init
from time import sleep
import subprocess
import sys
init(autoreset=True)
ascii_banner = pyfiglet.figlet_format("Fell's Toolkit")
print(Fore.RED + ascii_banner)
print(Fore.WHITE + "By: Fellcrack")
sleep(2)
primeravez = str(input("Is this your first time using the toolkit? (y/n): "))
if primeravez == "y":
    print(Fore.RED + "Installing required libraries...")
    sleep(2)
    os.system("pip install colorama")
    os.system("pip install pyfiglet")
    os.system("pip install scapy")
    os.system("pip install pynput")
    os.system("pip install pywin32")
    os.system("pip install pyinstaller")
    os.system("pip install smtplib")
    os.system("mkdir /usr/share/doc/Fell's Toolkit/")
    print(Fore.RED + "Libraries installed successfully!")
    
    sleep(2)
    print(Fore.RED + "Restarting the toolkit...")
    sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
elif primeravez == "n":
    print(Fore.RED + "Starting the toolkit...")
    sleep(2)
else:
    print(Fore.RED + "Invalid option. Please enter 'y' or 'n'.")
    sleep(2)
    print(Fore.RED + "Restarting the toolkit...")
    sleep(2)
    os.execl(sys.executable, sys.executable, *sys.argv)
print('''
[1] Web vuln scanners
[2] Nmap
[3] Deauth tool
[4] spam tool
[5] Exit
      
''')
opcion = str(input("Choose an option: "))
def web_vuln_scanners():
    print(Fore.RED + "Opening web vulnerability scanners...")
    sleep(2)
    ip = str(input("Enter the target IP: "))
    target = str(input("Enter the target name (without spaces): "))
    os.system("cd /usr/share/doc/Fell's Toolkit/")
    os.system("nmap --script http-vuln* ", ip ,"-oN nmap_web_vuln_scan", target ,".txt")
    os.system("nikto -h ", ip ,"-output nikto_scan", target ,".txt")
    os.system("whatweb -v ", ip ," > whatweb_scan", target ,".txt")
    os.system("dirb http://", ip ," /usr/share/wordlists/dirb/common.txt -o dirb_scan", target ,".txt")
    os.system("wapiti -u http://", ip ," -o wapiti_scan", target ,".html")
    print(Fore.RED + "Scans completed! Check the /usr/share/doc/Fell's Toolkit/ directory for results.")
    sleep(2)

def nmap_scan():
    print(Fore.RED + "Opening Nmap scanner...")
    sleep(2)
    ip = str(input("Enter the target IP: "))
    target = str(input("Enter the target name (without spaces): "))
    os.system("cd /usr/share/doc/Fell's Toolkit/")
    os.system("nmap -sC -sV -oN nmap_full_scan", target ,".txt ", ip)
    os.system("nmap -p- -oN nmap_all_ports_scan", target ,".txt ", ip)
    os.system("nmap --script vuln -oN nmap_vuln_scan", target ,".txt ", ip)
    os.system("nmap --script smb-vuln* -oN nmap_smb_vuln_scan", target ,".txt ", ip)
    print(Fore.RED + "Scans completed! Check the /usr/share/doc/Fell's Toolkit/ directory for results.")
    sleep(2)
def deauth_tool():
    print(Fore.RED + "Opening Deauth tool...")
    sleep(2)
    os.system("cd /usr/share/doc/Fell's Toolkit/")
    os.system("python3 Deauth tool/Deauth_sub.py")