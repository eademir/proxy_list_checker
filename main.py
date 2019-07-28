import os

b = input("file name:")
d = input("file format:")
a = open(b + "." + d, "r")
c = open("server's_up.txt", "a")

with a as f:
   for hostname in f:
       response = os.system("ping -c 1 " + hostname)

       if response == 0:
           print(hostname, 'is up!')
           c.write(hostname)
       else:
           print(hostname, 'is down!')
