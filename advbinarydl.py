#!/usr/bin/env python
# Advanced binary download - Chapter 17 - advbinarydl.py

import os, sys
from ftplib import FTP


f = FTP('10.22.21.56')
f.login()

f.cwd('/pub/louisefile')
f.voidcmd("TYPE I")

datasock, size = f.ntransfercmd("RETR remote_file.txt")
bytes_so_far = 0
# print(datasock)
with open('remote_file.txt', 'wb') as fd:
    while 1:
        buf = datasock.recv(2048)
        if not buf:
            break
        fd.write(buf)
        bytes_so_far += len(buf)
        print("Received", bytes_so_far, end = ' ')
        if size:
            print("of %d total bytes (%.1f%%)" % (
                size, 100 * bytes_so_far / float(size)))
        else:
            print("bytes", end=' ')
        sys.stdout.flush()

print()
datasock.close()
f.voidresp()
f.quit()
