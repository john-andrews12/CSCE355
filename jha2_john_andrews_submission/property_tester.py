#code written by John Andrews
#last updated on Dec 5 2018
#This file is a basic wrapper for the files that do the reading of data
#and subsequent execution of that data to test the properties of the dfa.

from file_reader_dfa import *
from dfa import *
from properties import *

#build the DFA
dfa_info = get_dfa_info()
dfa = DFA(dfa_info[2],dfa_info[3],dfa_info[1])

#do appropriate tests
if determine_empty(dfa):
	print("empty ",end="")
else:
	print("nonempty ",end="")

if determine_infinite(dfa):
	print("infinite")
else:
	print("finite")