def bmi_calculator():
    height = input('please enter your height in m: ')
    weight = input('please enter your weight in kg: ')
    bmi = int(weight) / float(height) ** 2
    bmi_as_int = int(bmi)
    print(f'your bmi is {bmi}')
    print(f'your bmi as int is {bmi_as_int}')


if __name__ == '__main__':
    print(bmi_calculator())