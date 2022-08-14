'''
# Instructions

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

## Warning. 

Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

**Example Input**
39
**Example Output**
3 + 9 = 12

12
e.g. When you hit run, this is what should happen:



Hint
Try to find out the data type of two_digit_number.
Think about what you learnt about subscripting.
Think about type conversion.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-2-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.'''


def add_two_digits(two_digit_number):
    two_digit_number = input('Type a two digit number: ')
    first_digit = two_digit_number[0]
    second_digit = two_digit_number[1]
    print(first_digit)
    print(second_digit)
    sum = int(first_digit) + int(second_digit)
    print(sum)
    

if __name__ == '__main__':
    print(add_two_digits(25))