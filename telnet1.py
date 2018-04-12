import getpass
import sys
import telnetlib

HOST = "10.1.1.1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("int loop0\n")
tn.write("ip addr 1.1.1.1 255.255.255.255\n")
tn.write("no shut\n")
tn.write("exit\n")
tn.write("int loop1\n")
tn.write("ip addr 2.2.2.2 255.255.255.255\n")
tn.write("no shut\n")
tn.write("exit\n")
tn.write("end\n")

