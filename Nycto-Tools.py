#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from os import system
from sys import exit

print "███╗   ██╗██╗   ██╗ ██████╗████████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗"
print "████╗  ██║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝"
print "██╔██╗ ██║ ╚████╔╝ ██║        ██║   ██║   ██║       ██║   ██║   ██║██║   ██║██║     ███████╗"
print "██║╚██╗██║  ╚██╔╝  ██║        ██║   ██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║"
print "██║ ╚████║   ██║   ╚██████╗   ██║   ╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║"
print "╚═╝  ╚═══╝   ╚═╝    ╚═════╝   ╚═╝    ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝"
                                                                                            
    
while True: 
    print "Nycto-Dork"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/nycto-dork")
        cd /Nycto-Tools/nycto-dork/nyctodork.py
        break

    
while True: 
    print "Nycto-Host"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Host")
        cd /Nycto-Tools/Nycto-Host/Nycto-Host/nyctohost.py
        break
     
    
while True: 
    print "Nycto-Map"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/NyctoMap")
        cd /Nycto-Tools/NyctoMap/nyctomap/nyctomap.sh
        break
     
    
while True: 
    print "Nycto-Stryke"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Stryke")
        cd /Nycto-Tools/Nycto-Stryke/Nycto-Stryke/nyctostryke.py
        break

    
while True: 
    print "Nycto-Brute"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/nycto-brute")
        cd /Nycto-Tools/nycto-brute/nycto-brute/nycto-brute.py
        break

while True: 
    print "Sql Enforcer"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Sqli-Enforcer")
        cd /Nycto-Tools/Sqli-Enforcer/Enforcer.py
        break
    
while True:  
    print "Nycto-WiFi"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-WiFi-Pwn")
        cd /Nycto-Tools/Nycto-WiFi-Pwn/Nycto-WiFi-Pwn/nycto-wifi.sh
        break

while True:
    print "Back The Box -HTB- Invite Key"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/HTB-INVITE")
        cd /Nycto-Tools/HTB-INVITE/HTB.py
        break
        
while True:
    print "Nycto Priv"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Priv")
        cd /Nycto-Tools/Nycto-Priv/nyctopriv.py
        break

while True: 
    print "Nycto-Gen"
    print "\n(1) Kali Linux x32/x64\n(2) Ubuntu / Parrot OS\n(3) Mac OS X / Darwin\n(0) Uninstall\n"
    getos = raw_input(">>")
    if getos == "1":
        system("sudo git clone https://github.com/nycto-hackerone/Nycto-Gen")
        cd /Nycto-Tools/Nycto-Gen/nyctogen/nyctogen.py

    break 
else:
    

    print "\nDone!"
exit(0)
