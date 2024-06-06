# Basic connection - Chapter 17 - connect.py 
from ftplib import FTP 
f = FTP('10.22.21.56') 

print("Welcome:", f.getwelcome() )
f.login()


print("Current working directory:", f.pwd() )
f.quit() 
