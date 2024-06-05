#!/usr/bin/env python
# Binary download - Chapter 17 - binaryul.py

from ftplib import FTP
import sys, getpass, os.path

if len(sys.argv) != 5:
    print("usage: %s <host> <username> <localfile> <remotedir>" % (
        sys.argv[0]))
    exit(2)

host, username, localfile, remotedir = sys.argv[1:]
password = getpass.getpass(
    "Enter password for %s on %s: " % (username, host))

f = FTP(host)
f.login(username, password)
f.cwd(remotedir)

with open(localfile, 'rb') as fd:
    f.storbinary('STOR %s' % os.path.basename(localfile), fd)

# check
f.retrlines('LIST')
f.quit()
