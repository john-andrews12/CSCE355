#code written by John Andrews
#last updated on Dec 5 2018
#This file contains code for a basic DFA class. It has pertinent information
#such as the start state, the transition function, and the final states.
#The states are assumed to be 0 through n-1 where n is the number of states.
#The alphabet is implicit within the transition table.

class DFA:
	#instance variables
	start_state_ = None
	transition_ = None
	finals_ = None
	
	#FUNCTION :: init
	#PARAMETERS
	#	alphabet - this is the string containign all symbols in the alphabet for the DFA
	#	transit - this should be a list containing the lines of the 'raw' description of
	#		the DFA's transition from the input file
	#	fin - this should be a list of strings representing the final state numbers
	#DESCRIPTION
	#	this function calls internal methods to set up the properties of a DFA from the
	#	the required material
	def __init__(self,alphabet,transit,fin):
		self.start_state_ = 0 #given in the project description
		self.build_transitions(alphabet,transit)
		self.set_finals(fin)
	
	#FUNCTION :: run_input
	#PARAMETERS
	#	inputt - this is the string of characters from the alphabet to push through the DFA
	#DESCRIPTION
	#	from the DFA's start state, this function loops through an input string and prints
	#	accept or reject depending on the end state the string exits in
	def run_input(self,inputt):
		curr_state = self.start_state_
		
		for x in inputt:
			curr_state = self.transition_[curr_state][x]
		
		if curr_state in self.finals_:
			print("accept")
		else:
			print("reject")
	
	#FUNCTION :: run_inputs
	#PARAMETERS
	#	inputs - this is a list of strings to test against the DFA
	#DESCRIPTION
	#	a wrapper function for the 'run_input' method to test a lot of inputs
	def run_inputs(self,inputs):
		for x in inputs:
			self.run_input(x)
	
	#FUNCTION :: build_transitions
	#PARAMETERS
	#	alpha - this is the alphabet for the DFA
	#	transit_raw - this should be a list containing the lines of the 'raw' description of
	#		the DFA's transition from the input file
	#DESCRIPTION
	#	This function takes the alphbet and the raw description of the transitions table and
	#	creates a list of dictionaries. The list indexes indicate state number, i.e. stage 
	#	zero's data is at the zeroth index of the list. The dictionaries map from character
	#	in the alphabet to state numbers.
	def build_transitions(self,alpha,transit_raw):
		self.transition_ = []
		for trans in transit_raw:
			temp = {}
			i = 0
			to = trans.split()
			for x in alpha:
				temp[x] = int(to[i])
				i+=1
			self.transition_.append(temp)
	
	#FUNCTION :: set_finals
	#PARAMETERS
	#	fin - this should be a list of strings representing the final state numbers
	#DESCRIPTION
	#	This function sets the DFA's finals to be an array of integers by converting the
	#	list of strings to ints
	def set_finals(self,fin):
		self.finals_ = []
		for x in fin:
			self.finals_.append(int(x))
	
	#this is an accessor to the built transitions table
	def get_transit_tab(self):
		return self.transition_
	
	#this is an accessor to the final or accepting states of the DFA
	def get_finals(self):
		return self.finals_
	
	#this is an accessor to the alphabet of the DFA
	def get_alpha(self):
		#loop through the transit table and build the alphabet and return it
		ret = []
		for x in self.transition_[0]:
			ret.append(x)
		return ret