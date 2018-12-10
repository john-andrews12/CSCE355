#code written by John Andrews
#last updated on Dec 5 2018
#This file is a basic wrapper for the files that do the reading of data
#and subsequent execution of that data to test the geration of a text searching DFA.

from file_reader_tsearch import *
from text_search import *

fline = get_first_line()
description = generate_output(fline)

print(description)