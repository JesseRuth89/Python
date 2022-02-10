"""
You are given an array of integers.
You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).
Input: A list of integers.
Output: The number as an integer.
"""

def checkio(array):
    num = []
    for i in range(len(array)):
        if i % 2 == 0:
            num.append(int(array[i]))

    if len(array) == 0:
        return(0)
    else:
        #return(sum(num) * array[len(array) -1])
        return(sum(num) * array[-1])
    
print(checkio([0, 1, 3,]))
print(checkio([]))
print(checkio([1, 1, 1, 1, 5, 7, 9, 3, 1]))

"""
Same Solution using slices

"""

def checkio(array):
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0

