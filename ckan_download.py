import requests

def download_and_save(filename):
  registry = download()
  with open(filename, 'w') as f:
    f.write(registry.encode('utf-8'))


def download():
  r = requests.get('http://data-gov-ua.org/dataset/9b09e9f7-e125-4d6f-8b3f-76ebee34aab0/resource/0e61d380-538c-46b4-96fa-80e3c722b588/download/koatuu122014.csv')
  r.encoding = 'utf-8'
  return r.text

if __name__ == '__main__':
  print 'Downloading...'
  download_and_save('koatuu.csv')
