#!/usr/bin/env python
# encoding=utf-8

import sys

def transform(input_filename, output_filename, regions_filename):
  of = open(output_filename, 'w')
  of.write(','.join(('рівень 1','рівень 2','рівень 3','рівень 4', 'Назва')) + '\n')
  rf = open(regions_filename,'w')
  rf.write(','.join(('Код', 'Назва')) + '\n')
  with open(input_filename, 'r') as f:
    for line in f.readlines()[1:]:
      items = line.replace('\0','').replace('"', '').split(',')
      if len(items) == 3:
        code, type_, name = items
      elif len(items) == 4:
        code, type_, name, desc = items
      elif len(items) == 5:
        code, type_, name, desc, _ = items
      else:
        pass
      region1_code = '%02d' % (int(code) / 100000000)
      region2_code = '%03d' % ((int(code) % 100000000) / 100000)
      region3_code = '%03d' % ((int(code) % 100000) / 1000)
      region4_code = '%02d' % (int(code) % 100)
      #if type_:
      #  type__ = {'Щ'}
      #print name
      of.write((','.join(map(lambda x: '"' + x + '"', (region1_code, region2_code, region3_code, region4_code, name.strip())))) + '\n')

      if int(region2_code) == 0:
        base_name = unicode(name.strip().split('/')[0].decode('utf-8'))
        base_name = base_name.split('.')
        if len(base_name) == 2:
          base_name = base_name[1]
        else:
          base_name = base_name[0]
        base_name = base_name.lower().title()
        rf.write('"' + region1_code + '",' + base_name.encode('utf-8') + '\n')

  of.close()
  rf.close()
      
    


if __name__ == '__main__':
  filename = sys.argv[1]
  formatted = sys.argv[2]
  regions = sys.argv[3]
  print 'Transforming %s...' % filename
  transform(filename, formatted, regions)
  print 'Transformed to %s, %s' % (formatted, regions)
