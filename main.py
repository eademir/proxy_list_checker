import os

b = input("file name:")
d = input("file format:")
c = open("server's_up.txt", "a")

with open(b + "." + d, "r") as f:
   for hostname in f:
       response = os.system("ping -c 1 " + hostname)
       if response == 0:
           c.write(hostname)