#!/usr/bin/python
import sys
import fileinput
import re

my_file= sys.argv[1]

for each_line_of_text in fileinput.input(my_file):
  if re.match(r'.*\t.*\tgene\t', each_line_of_text):
        gene_name_matches = re.findall ('gene_name \"(.*?)\";', each_line_of_text)
        chromosome_matches = re.findall ('^.', each_line_of_text)
        startPos_matches = re.findall ('.*\t.*\tgene\t(\d\d\d\d\d)\s', each_line_of_text)
        endPos_matches = re.findall ('.*\t.*\tgene\t(\d\d\d\d\d)\s(\d\d\d\d\d)', each_line_of_text)
[
        print 'gene_name', + gene_name_matches
        print 'chromosome' + chromosome_matches
        print 'startPos ' + startPos_matches
        print 'endPos ' + endPos_matches
]
