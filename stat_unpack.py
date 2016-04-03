#!/usr/bin/python

from zipfile import ZipFile
from distutils.dir_util import mkpath
import sys

def unpack(filename, directory):
  mkpath(directory)  
  with ZipFile(filename, 'r') as myzip:
    myzip.extractall(directory)

if __name__ == '__main__':
  filename = sys.argv[1]
  folder = sys.argv[2]
  print 'Extracting %s...' % filename
  unpack(filename, folder)
  print 'Extracted to %s' % folder
