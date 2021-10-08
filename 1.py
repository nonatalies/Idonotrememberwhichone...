array = []
flag = True
while flag:
    try:
        length = abs(int(input("Enter number of elements in array : ")))
        flag = False
    except ValueError:
        print("Error, should be a number.")

i = 0
while i < length:
    try:
        element = int(input("Element: "))
        array.append(element)
        i = i + 1
    except ValueError:
        print("Error, should be a number.") 

flag = True
while flag:
    try:
        delta = abs(int(input("Enter delta : ")))
        flag = False
    except ValueError:
        print("Error, should be a number.")
        
minValue = min(array)
print("Min element from array: ", minValue)

res = 0
for i in range(0, length):
    if ((array[i] - minValue) == delta):
        res = res + 1

print("Result: ", res)
