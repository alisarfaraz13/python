#! /usr/bin/env python

import openpyxl

#read data from db, text, json file
# text has data with pipe delimited
#
#   counter = 0
# with open('filename','r') as fh:

#   for line in fh:
#   counter = counter + 1
#   line.split('|')
#    line[0]
#    sheet['A'+ counter] = line[0]

wb = openpyxl.load_workbook('example1.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

stimulusTimes = [1, 2, 3, 4]
reactionTimes = [2.3, 5.1, 7.0, 5.0]

for i in range(len(stimulusTimes)):
    print "valur",i
    sheet['A' + str(i + 6)].value = stimulusTimes[i]
    sheet['B' + str(i + 6)].value = reactionTimes[i]

wb.save('example1.xlsx')

print range(3)
