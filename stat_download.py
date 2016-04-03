#!/usr/bin/env python
import requests
import sys
from distutils.dir_util import mkpath
import os

def download_and_save(url, filename):
  registry = download(url)
  mkpath(os.path.dirname(filename))
  with open(filename, 'w') as f:
    f.write(registry)


def download(url):
  r = requests.get(url)
  return r.content

if __name__ == '__main__':
  url = sys.argv[1]
  filename = sys.argv[2]
  print 'Downloading %s...' % url
  download_and_save(url, filename)
  print 'Downloded to %s' % filename
