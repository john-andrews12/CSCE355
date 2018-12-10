#code written by John Andrews
#last updated on Dec 5 2018
#This file is a basic wrapper for the files that do the reading of data
#and subsequent execution of that data to test the simulation of the dfa.

from file_reader_dfa import *
from dfa import *

dfa_info = get_dfa_info()
input_lines = get_input_lines()

dfa = DFA(dfa_info[2],dfa_info[3],dfa_info[1])
dfa.run_inputs(input_lines)