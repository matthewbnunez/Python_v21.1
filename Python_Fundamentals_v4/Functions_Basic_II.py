# Countdown
def countdown(num):
    arr = [];
    for i in range(num, -1, -1):
        arr.append(i)
    return arr
    
print(countdown(5))


# Print and Return
def printAndReturn(num):
    num2 = num.pop()
    print(num[0])
    return num2

print(printAndReturn([1,2]))


# First Plus Length
def firstPlusLength(num):
    return num[0] + len(num)

print(firstPlusLength([1,2,3,4,5]))


# Values Greater than Second
def valuesGreaterThanSecond(arr, min):
    greater_than_second = []
    if len(arr) < 2:
        return False
    for x in range(0, len(arr)):
        if arr[x] >= min:
            greater_than_second.append(arr[x])
    print(len(greater_than_second))
    return greater_than_second

print(valuesGreaterThanSecond([5,2,3,2,1,4], 3))
print(valuesGreaterThanSecond([3], 3))


# This Length, That Value 
def lengthAndValue(size, value):
    arr = []
    for x in range(0, size):
        arr.append(value)
    return arr

print(lengthAndValue(4, 7))
print(lengthAndValue(6, 2))