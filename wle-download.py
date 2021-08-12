#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
import json
import openpyxl
import xlrd
import wget
import urllib
import time


i = 1
loc = ('wle.xlsx')
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(i, 2))

ext = sheet.cell_value(i, 2)[len(sheet.cell_value(i, 2)) - 4:]
url= sheet.cell_value(1, 2)
print(ext)
for i in range(sheet.nrows):
    #print(sheet.cell_value(i, 2))
    try:
        ur = sheet.cell_value(i, 2)
        wget.download(sheet.cell_value(i, 2))
    except IOError:
        print(sheet.cell_value(i, 2))

#filename = wget.download(ur)
# urllib.urlretrieve('', 'image' + ext)
