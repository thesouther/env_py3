#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:13:55 2017

@author: cc
"""


import xlrd
  
fname = "wk1.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
 sh = bk.sheet_by_name("Sheet1")
except:
 print("no sheet in %s named Sheet1" % fname)

nrows = sh.nrows
#获取列数
ncols = sh.ncols
print("nrows %d, ncols %d" % (nrows,ncols))
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)
#print cell_value
  
row_list = []
#获取各行数据
for i in range(1,nrows):
 row_data = sh.row_values(i)
 row_list.append(row_data)