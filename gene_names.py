#!/usr/bin/python
import sys
import fileinput
import re

output = {}
f = open (sys.argv[1],'r')
lines=f.readlines()
for each_line_of_text in lines:
  if re.search(r'.*\t.*\tgene\t', each_line_of_text):
        geneName = re.findall (r'gene_name \"(.*?)\";', each_line_of_text)
        print "{\"geneName\":",
        print geneName,
        print ",",
        chromosome = re.findall (r'^(\d)', each_line_of_text)
        print "{\chromosome\":",
        print chromosome,
        print ",",
        startPos = re.findall (r'.*\t.*\tgene\t(\d\d\d\d\d)\s', each_line_of_text)
        print "{\startPos\":",
        print startPos,
        print ",",
        endPos = re.findall (r'.*\t.*\tgene\t(\d\d\d\d\d)\s(\d\d\d\d\d)', each_line_of_text)
        print "{\endPos\":",
        print endPos,
        print ",",
        print "}"
