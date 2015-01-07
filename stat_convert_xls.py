#!/usr/bin/python
from pyexcel_xls import get_data
import csv

def convert_row(row):
  try:
    code = u"%d" % row[0]
  except TypeError:
    code = u"%s" % row[0]
  code_type = u"%s" % row[1]
  name = u"%s" % row[2]
  return code, code_type, name

if __name__ == '__main__':
  filename = './data/koatuu/KOATUU_DBF_122015.xls'
  output_filename = './data/koatuu_122015.csv'
  print 'Converting xls to csv...'
  data = get_data(filename)
  koatuu = data['Sheet1']
  koatuu = map(convert_row, koatuu)
  with open(output_filename, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in koatuu:
      writer.writerow([s.encode("utf-8") for s in row])
  print 'Converted %s to %s' % (filename, output_filename)
