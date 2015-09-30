#asking the user to enter a word
a = input("Enter a word to check\n")

#[::-1] stores the reverse of
# a string into a new string
reverse_word = a[::-1]

#if statement to check if the 
#word is a palendrome
if a == reverse_word:
	result = True
	print (result)
else:
	result = False
	print (result)
