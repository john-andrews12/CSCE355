#code written by John Andrews
#last updated on Dec 5 2018
#This file contains code for reading in and parsing a DFA description as 
#defined in the project description. In addition, this file contains code for 
#reading in lines to test the DFA with.

import sys

def get_dfa_info():
	file_name = sys.argv[1]
	
	file = open(file_name, "r")
	
	line = file.readline()
	num_states = line[18:]
	
	line = file.readline()
	final_states = line.split()
	final_states.remove("Accepting")
	final_states.remove("states:")
	
	line = file.readline()
	alphabet = line[10:]
	if alphabet[-1:] is '\n':
		alphabet = alphabet[:-1]#remove the \n char from the string
	
	transitions = []
	for i in range(0, int(num_states)):
		tran = file.readline()
		if tran[-1:] is '\n':
			tran = tran[:-1]#remove the \n char from the string
		transitions.append(tran)
	
	output = [num_states, final_states, alphabet, transitions]
	
	return output

def get_input_lines():
	file_name = sys.argv[2]
	
	file = open(file_name, "r")
	
	output = []
	
	for line in file:
		if line[-1:] is '\n':
			line = line[:-1]#remove the \n char from the string
		output.append(line)
	
	return output