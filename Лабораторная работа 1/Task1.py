numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum = 0
k = 0
for i in range(len(numbers)):
    if type(numbers[i]) == int:
        sum = sum + numbers[i]
    else:
        k = i
numbers[k] = sum/len(numbers)
print("Измененный список:", numbers)
