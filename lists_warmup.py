numbers = [3, 1, 4, 1, 5, 9, 2]
''' 1. Change the first element of numbers to "ten" (the string, not the number 10)'''
numbers[0] = "ten"
print(numbers[0])
''' 2.Change the last element of numbers to 1'''
numbers[-1] = 1
print(numbers[-1])
''' 3.Get all the elements from numbers except the first two (slice)'''
print(numbers[2:])
''' 4.Check if 9 is an element of numbers'''
if 9 in numbers:
    print(True)


