#!/usr/bin/env python
# ASCII download - Chapter 17 - asciidl.py
# Downloads README from remote and writes it to disk.

import os
from ftplib import FTP

if os.path.exists('test.txt'):
    raise IOError('refusing to overwrite your file')

def writeline(data):
    fd.write(data)
    fd.write(os.linesep) 

f = FTP('10.22.21.56')
f.login()
f.cwd('/pub/class')

fd = open('test.txt', 'w')
f.retrlines('RETR remote_file.txt', writeline)
fd.close()

f.quit()
