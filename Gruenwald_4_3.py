digits = [int(element) for element in input("Введите числа: ").split()]
el = int(input("Задайте число: "))
counter = digits[0]
for num in digits:
    if abs(num - el) < abs(counter - el):
        counter = num
print("самое близкое по величине число: ", counter)