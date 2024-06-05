#!/usr/bin/env python
# ASCII download - Chapter 17 - asciidl.py
# Downloads README from remote and writes it to disk.
import os
from ftplib import FTP

ftp = FTP('10.22.21.56')
ftp.login()

ftp.cwd('/pub/louisefile')

with open('local_file.txt', 'w') as fd:
    ftp.retrlines('RETR remote_file.txt', fd.write)

ftp.quit()
