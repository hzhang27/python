#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

【作者】 ZHANG Hui
【版本】 2017-7-03
 
"""
 

import sys;
import argparse;
import re
import getopt,sys

def wordCalc():	  

    newParser = argparse.ArgumentParser();
    newParser.add_argument("-s", "--source", dest="source", help="source file need to be processed");
    newParser.add_argument("-o", "--output", dest="output", help="out file");
    args = newParser.parse_args();
 
     
    print ("args=",args); 
    print ("type(args)=",type(args)); 
     
    argsDict = args.__dict__;
    print ("parsed argsDict=",argsDict); 
     
    for eachArg in argsDict.keys():
        exec(eachArg + " = args." + eachArg);
 
    inFile = open(argsDict['source'])
    dic = {}
    rc = re.compile(r'[a-zA-Z]+',re.I)
    for line in inFile:
    	words = rc.findall(line)
    	for word in words:
    		if word in dic:
    			dic[word] += 1
    		else:
    			dic[word] = 1
    inFile.close()
    
    outfile = open(argsDict['output'], 'w')
    outfile.write('word,count\n')
    for k in sorted(dic.items(), key=lambda d: d[1], reverse = True):
    	print (k)
    	outfile.write('%s,%d' %k)
    	outfile.write('\n')
    outfile.close()
	
	
###############################################################################
if __name__=="__main__":
    wordCalc();