from hashlib import new


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