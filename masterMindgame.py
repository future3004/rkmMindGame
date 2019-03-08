# /usr/bin/python
# this is a web-based python script for the game

print 'Content-type: text/html'
print ''

import cgi
import random
form = cgi.FieldStorage() 

reds = 0
whites = 0
message = ""

if "answer" in form:
	answer = form.getvalue("answer")
else:
	# generating a string of 4 random numbers and add it to answer variable
	answer = ""
	for i in range(4):
		answer += str(random.randint(0, 9))

print(answer)

# getting the get variable value
if "guess" in form:
	guess = form.getvalue("guess")
	for key, digit in enumerate(guess):     # comparing answer and user guess
		if digit == answer[key]:
			reds += 1
		else:
			for answerDigit in answer:
				if answerDigit == digit:
					whites += 1
					break

else:
	guess = ""



# keeping track of number of user guesses
if "count" in form:
	count = int(form.getvalue("count")) + 1
else:
	count = 0

# print(reds)
# print(whites)
if count == 0:
	message = "I've chosen a 4 digit number. Can you guess it?"
elif reds == 4:
	message = "You've WON!! You got it in " + str(count) + " guesses. <a href=''>Play again</a>"
else:
	message = "You have " + str(reds) + " correct digit(s) in the right place, and " +
	str(whites) + " correct digit(s) in the wrong place. You have had " +
	str(count) + " guess(es)."


# building the simple user interface with html
print '<h1>My Game!</h1>'
print "<p>" + message + "</p>"
print '<form method="post">'
print '<input type="text" name="guess" value="' + guess + '">'
print '<input type="hidden" name="answer" value="' + answer + '">'
print '<input type="hidden" name="count" value="' + str(count) + '">'
print '<input type="submit" value="Guess!">'
print '</form>'

# end of script