#!/usr/bin/env python
# ASCII download - Chapter 17 - asciidl.py
# Downloads README from remote and writes it to disk.
from ftplib import FTP

f = FTP('10.22.21.56')
f.login()

f.cwd('/pub/class')

with open('test.txt', 'w') as fd:
    f.retrlines('RETR remote_file.txt', fd.write)

f.quit()
