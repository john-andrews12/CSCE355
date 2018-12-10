#code written by John Andrews
#last updated on Dec 5 2018
#This file contains code for determining properties about a DFA.

import queue

def determine_empty(input_dfa):
	finals = input_dfa.get_finals()
	
	#is the start state is a final, then the language is certainly not empty due to epsilon
	if 0 in finals:
		return False
	
	visitable_states = get_reachability_from(input_dfa,0)
	
	empty = True
	if overlap(finals, visitable_states):
		empty = False
	
	return empty

def get_reachability_from(input_dfa,state):
	transit_tab = input_dfa.get_transit_tab()
	
	states_to_check = queue.Queue()
	states_to_check.put(state)
	visitable_states = []
	
	while not states_to_check.empty():
		current = states_to_check.get()#current state we're looking out from
		cur_row = transit_tab[current]#all the transitions that could be made from there
		
		for x in cur_row:
			if cur_row[x] not in visitable_states:
				states_to_check.put(cur_row[x])
				visitable_states.append(cur_row[x])
	
	return visitable_states

def determine_infinite(input_dfa):
	infinite = False
	
	if determine_empty(input_dfa):#if it is empty, it is certainly not infinite
		return infinite
	
	reachability_by_state = []
	num_states = len(input_dfa.get_transit_tab())
	
	for x in range(0, num_states):
		reach = get_reachability_from(input_dfa,x)
		reachability_by_state.append(reach)
	
	#determine the finals that actually matter
	visitable_states = reachability_by_state[0]
	finals = input_dfa.get_finals()
	reachable_finals = []
	
	for x in finals:
		if x in visitable_states:
			reachable_finals.append(x)
	
	#look for states that meet the requirements for infinite
	for x in range(0,num_states):
		if x in reachability_by_state[x]:#if there is a loop
			if x in reachability_by_state[0]:#if the loop can be reached from the initial state
				if overlap(reachable_finals, reachability_by_state[x]):#if you can reach a final state
					infinite = True
	
	return infinite

def overlap(l1, l2):
	#this check is to keep the run time of this algorithm down to min len(l1),len(l2)
	if len(l1) < len(l2):
		for x in l1:
			if x in l2:
				return True
	else:
		for x in l2:
			if x in l1:
				return True
	return False



