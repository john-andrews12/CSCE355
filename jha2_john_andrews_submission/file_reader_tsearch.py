#code written by John Andrews
#last updated on Dec 5 2018
#This file contains code for reading in the string that will define
#the text searcher DFA. It pretty much just gets a single word from the file.

import sys

def get_first_line():
	file_name = sys.argv[1]
	
	file = open(file_name, "r")
	
	line = file.readline()
	
	if line[-1:] is '\n':
		line = line[:-1]
	
	return line