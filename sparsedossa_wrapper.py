#!/usr/bin/env python

"""
Author: Simon Chang and George Weingart
Description: Wrapper program for sparseDOSSA
"""

#####################################################################################
#Copyright (C) <2016>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use, copy,
#modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies
#or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#####################################################################################

__author__ = "Simon Chang and George Weingart"
__copyright__ = "Copyright 2016"
__credits__ = ["Simon Chang and George Weingart"]
__license__ = "MIT"
__maintainer__ = "Simon Chang and George Weingart"
__email__ = "george.weingart@gmail.com"
__status__ = "Development"

from cStringIO import StringIO
import sys,string
import os
import tempfile 
from pprint import pprint
import argparse

######################################################################################
#  Parse input parms                                                                 #
######################################################################################
def read_params(x):
	parser = argparse.ArgumentParser(description='sparseDOSSA Argparser')
	parser.add_argument('--features', action="store", type=int,default=150,dest='features',nargs='?')
        parser.add_argument('--samples', action="store", type=int,default=180,dest='samples',nargs='?')
        parser.add_argument('--metadata', action="store", type=int,default=10,dest='metadata',nargs='?')
        parser.add_argument('--output1', action="store", dest='output1',nargs='?')
        parser.add_argument('--output2', action="store", dest='output2',nargs='?')
        parser.add_argument('--output3', action="store", dest='output3',nargs='?')
	return  parser




######################################################################################
#   Main  Program                                                                    #
######################################################################################

# Parse commandline in
parser = read_params( sys.argv )
results = parser.parse_args()
root_dir = "//usr/local/galaxy-dist/tools/sparsedossa"




### Define directory locations
D = os.path.join(root_dir)
DSrc = os.path.join(root_dir,"sparsedossa","R")
Dsparsedossa = os.path.join(root_dir)



### Build sparsedossa
CmdsArray = [\
os.path.join(DSrc,"synthetic_datasets_script.R"),  \
"-f", str(results.features),\
"-n", str(results.samples),\
"-p", str(results.metadata), \
">/dev/null",\
"2>&1"
]

invoke_sparsedossa_cmd = " ".join(CmdsArray)



CurrDir=os.getcwd()



### Call sparsedossa
os.system(invoke_sparsedossa_cmd)





### Copy output file to make available to galaxy
o1 =  os.path.join(CurrDir,"LognormalWithOutliers.pdf")
cmd_copy1 = "cp " + o1 + " " + results.output1
os.system(cmd_copy1)


o2 = os.path.join(CurrDir, "SyntheticMicrobiome-Counts.pcl")
cmd_copy2 = "cp " + o2 + " " + results.output2
os.system(cmd_copy2)


o3 = os.path.join(CurrDir,"SyntheticMicrobiomeParameterFile.txt")
cmd_copy3 = "cp " + o3 + " " + results.output3
os.system(cmd_copy3)


