def bmi_calculator():
    height = input('please enter your height in m: ')
    weight = input('please enter your weight in kg: ')
    bmi = int(weight) / int(height) ** 2
    print(f'your bmi is {bmi}')


if __name__ == '__main__':
    print(bmi_calculator())