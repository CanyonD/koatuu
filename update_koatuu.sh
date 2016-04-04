#!/usr/bin/env sh
set -e
rm -rf tmp/
./stat_download.py http://www.ukrstat.gov.ua/klasf/st_kls/koatuu.zip ./tmp/koatuu.zip
./stat_unpack.py ./tmp/koatuu.zip ./tmp/koatuu
./stat_convert_xls.py ./tmp/koatuu/KOATUU_*.xls ./tmp/koatuu.csv

rm -rf output/
mkdir -p output/
./transform.py tmp/koatuu.csv output/koatuu_full.csv output/koatuu_regions.csv
