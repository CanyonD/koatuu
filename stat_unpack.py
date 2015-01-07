#!/usr/bin/python
from zipfile import ZipFile
from distutils.dir_util import mkpath

def unpack(filename, directory):
  mkpath(directory)  
  with ZipFile(filename, 'r') as myzip:
    myzip.extractall(directory)

if __name__ == '__main__':
  print 'Unpacking...'
  folder = './data/koatuu'
  filename = './data/koatuu.zip'
  unpack(filename, folder)
  print 'Extracted %s to %s' % (filename, folder)
