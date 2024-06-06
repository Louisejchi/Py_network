#!/usr/bin/env python
# Binary upload - Chapter 17 - binarydl.py

from ftplib import FTP


f = FTP('10.22.21.56')
f.login()
f.cwd('/pub/class')

with open('ncnu.png', 'wb') as fd:
    f.retrbinary('RETR ncnu.png', fd.write)

f.quit()
