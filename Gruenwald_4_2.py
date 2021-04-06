digits = [int(element) for element in input("Введите числа: ").split()]

for counter in range(0, len(digits), 2):
    print(digits[counter])