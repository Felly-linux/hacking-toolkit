import os
import time
from colorama import Fore, init
init()
def ssh_init():
    os.system("clear")
    IP = input(Fore.BLUE+("Put the SSH IP address to connect by SSH: "))
    PORT = input("Put the port to connect by SSH: ")
    USER = input("Choose the USER to conect by SSH: ")
    time.sleep(1)
    print(Fore.YELLOW+("IP address: ", IP))
    print("Port to connect: ", PORT)
    print("User to connect: ", USER)
    time.sleep(1)
    choice_ssh = input(str(Fore.BLUE+ ("Are you sure to proceed? (Y/n): ")))
    if choice_ssh == "y":
        os.system("ssh -p ", PORT ," ", USER ,"@", USER)
    if choice_ssh == "n":
        print(Fore.RED+("just press CTRL + C and exit"))
    else: 
        print(Fore.RED+("That's not an option..."))
