#!/usr/bin/python
from time import sleep
from os import system
from sys import exit

    
while True: 
    print "Nycto-Dork"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/nycto-dork")
        break

    
while True: 
    print "Nycto-Host"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Host")
        break
     
    
while True: 
    print "Nycto-Map"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/NyctoMap")
        break
     
    
while True: 
    print "Nycto-Stryke"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Stryke")
        break

    
while True: 
    print "Nycto-Brute"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/nycto-brute")
        break

    
while True:  
    print "Nycto-WiFi"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-WiFi-Pwn")
        break


while True: 
    print "Nycto-Gen"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Gen")

    break 
else:
    

    print "\nDone!"
exit(0)
