#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


menu = """

[1] HTTP Header Check
[2] Extract Page Links
[3] Exit
"""


print menu

def run():

    try:
        choice = input("Which option number : ")

       

        if choice == 1:
            print("\n")
            print("[+] HTTP Header Check script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/httpheaders/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 2:
            print("\n")
            print("[+] Extract Page Links script running..")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/pagelinks/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 3:
            exit()

    except KeyboardInterrupt:
        print("\nAborted!")
        quit()
    except:
        print("Invalid Optioin !\n")
        return run()
run()
