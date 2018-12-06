#code written by John Andrews
#last updated on Dec 5 2018
#This file contains code for the text search project. Within is a function that takes in a word and
#generates a DFA that accepts strings containing said word. I am sure there is so more efficient
#way of solving this problem but I know this method works. I wrote this code on the way home from 
#Thanksgiving and I'm sticking with it.

def generate_output(word):
	alphabet = "abcdefghijklmnopqrstuvwxyz"#per project description
	
	last_state = len(word)
	num_states = last_state+1#a state for the number of characters matched plus 1 for no matches
	
	transitions = []
	#give the entire table a default value of going back to the zero characters matched state
	for x in range(0,num_states):
		tran = {}
		for y in alphabet:
			tran[y] = 0 #give every transition a default setting of zeri
		transitions.append(tran)
	
	#the last state (aka the string has been matched) transitions to itself over the entire alphabet
	for x in transitions[last_state]:
		transitions[last_state][x] = last_state
	
	#create the substrings of the string, these will be used in evaluating transitions later on
	#note that the substrings are indexed by their length
	substrings = [""]#the empty string is a substring of everything
	accum = ""
	
	for x in word:
		accum += x
		substrings.append(accum)
	
	#loop through each substring and see where you can go by reading in any of the available letters
	for i in range(0,len(substrings)-1):
		#cur is the current match of the characters in the string being tested
		cur = substrings[i]
		#consider all of the possible next letters
		for x in alphabet:
			#so if x isn't in the word, then we are going to have to transition back to the no characters match 
			#state which is the default, zero. Thus we only need to do anything if x is a character in the word
			if x in word[:len(cur)+1]:
				curx = cur + x
				#check if a character will get you to the next substring
				if curx == substrings[i+1]:
					transitions[i][x] = i + 1
				else:
					#so the letter has been encountered, but it won't get us to the next state so we want to check
					#if adding it to the end of the string will make the end of our input string match with the 
					#start of the key match word
					largest = 0
					#we use j to loop backwards through the end of our current 'input' so we start by going from
					#the last letter to the entire string except for the first letter since if that matched a sub
					#string of that size it would have already been picked up in the if statement
					for j in range(1,i+1):
						#get the substring
						curx_end_sub = curx[-j:]
						#for k in range (1,j+1):
						if curx_end_sub == substrings[len(curx_end_sub)]:
							largest = len(curx_end_sub)
					transitions[i][x] = largest
	
	output = "Number of states: " + str(num_states) + "\nAccepting states: " + str(last_state) + "\nAlphabet: " + alphabet + "\n"
	
	for x in transitions:
		for y in x:
			output += str(x[y]) + " "
		output = output[:-1]#remove the last space
		output += '\n'
	
	output = output[:-1]#remove the trailing new line char
	
	return output
	