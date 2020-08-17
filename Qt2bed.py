#!/usr/bin/env python
# Copyright (C) <2020> PMBL;South China Agricultural University. All rights reserved
__author__ = "Write by Fangping Li"
__version__ = '0.1.0'

dic = {"A":"1  1","T":"2  2","C":"3  3","G":"4  4",
       "R":"1  4","Y":"2  3","M":"1  3","K":"4  2",
       "S":"4  3","W":"1  2","N":"0  0"}
import sys
goin = sys.argv[1]#INPUTFILE
goout1 = sys.argv[2]#OUTPUT OF SNPINFO
goout2 =  sys.argv[3]#OUTPUT OF SITE

file = open(goin,"r")
outfile1 = open(goout1,"w") 
outfile2 = open(goout2,"w")

lines = list(file.readlines())


for i in lines[2:]:
    i = i.split()
    print(i[0]+"	"+i[3],file = outfile1)
    
outfile1.close()    

for j in range(len(lines)):
    lines[j] = lines[j].split()
    
linesline = zip(*lines)
linesline = list(linesline)
for i in range(len(linesline)):
    linesline[i]=list(linesline[i])
    

count = 0
for i in linesline[11:]:
    count += 1
    temp = i[0] + "	" + str(count) + "	0	0	0	0"
    print(temp,file = outfile2,end = "	")
    for j in i[1:]:
        print(dic[j],file = outfile2,end = "	")
        
    print("",file = outfile2)
        
outfile2.close()
