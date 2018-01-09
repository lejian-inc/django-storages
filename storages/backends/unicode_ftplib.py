# encoding: utf-8
# in python2 ftplib don't support utf8, let's hack this
# TODO: for python3, it's save to use encoding
import ftplib


class FTP(ftplib.FTP):
    """A ftplib.FTP subclass supporting unicode file names as 
   described by RFC-2640."""

    def putline(self, line):
        if '\r' in line or '\n' in line:
            raise ValueError('an illegal newline character should not be contained')
        line = line + CRLF
        if isinstance(line, unicode):
            line = line.encode('utf8')
        if self.debugging > 1: print '*put*', self.sanitize(line)
        self.sock.sendall(line)

from ftplib import *
