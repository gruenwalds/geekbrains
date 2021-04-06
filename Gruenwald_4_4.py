digits = [int(element) for element in input("Введите числа: ").split()]
even_number = 0
sum_numbers = 0
for counter in digits:
    if counter % 2 == 0:
        even_number = even_number + counter
for nums in range(1, len(digits), 2):
    sum_numbers = sum_numbers + digits[nums]
sum_numbers = sum_numbers + even_number
print("Сумма чисел равна: ", sum_numbers)