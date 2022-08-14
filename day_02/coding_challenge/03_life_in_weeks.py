"""
Your Life in Weeks
UPDATE
We've moved away from repl.it for coding exercises. Check out the new exercises on Coding Rooms with automated submissions.


Instructions
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
e.g. When you hit run, this is what should happen:



Hint
There are 365 days in a year, 52 weeks in a year and 12 months in a year.
Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-2-3-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.


"""

age = input('what is your current age: ')
# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365
message = f'you have {days} days until 90, you have {weeks} weeks until 90, you have {months} months until 90, and you have {years} years until 90'

# calculate how many days, weeks, years until 90 years old

print(message)