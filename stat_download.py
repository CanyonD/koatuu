#!/usr/bin/python
import requests

def download_and_save(filename):
  registry = download()
  with open(filename, 'w') as f:
    f.write(registry)


def download():
  url = 'http://www.ukrstat.gov.ua/klasf/st_kls/koatuu.zip'
  r = requests.get(url)
  return r.content

if __name__ == '__main__':
  print 'Downloading...'
  filename = './data/koatuu.zip'
  download_and_save(filename)
  print 'Downloded %s' % filename
