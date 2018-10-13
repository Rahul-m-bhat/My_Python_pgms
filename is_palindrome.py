#This is a Program to find a palindrome of a String.
def palindrome(string):
	s = string.lower()
	s = s.replace(" ","")
	h = s[::-1]
	if s == h:
		print("the '%s' is a palindrome" % (string))
	else:
		print("the '%s' is not a palindrome" % (string))


#running the program with input as "nurses Run"
palindrome("nurses Run")

#running the program with input as "Today is a good day"
palindrome("Today is a good day")
