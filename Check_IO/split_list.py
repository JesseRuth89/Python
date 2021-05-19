"""
You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.
"""
import math
def split_list(items: list) -> list:
    # Checking to see if list is even
    if len(items) % 2 == 0:
        # Setting slice position to half
        position = round(len(items) / 2)
        # I prefer to assign vars instead of mashing it all into the return
        first_list = items[:position]
        second_list = items[position:]
        return [first_list, second_list]
    else:
        # If odd find the first half by rounding up
        # Lots of way to cut this cow, use math ceiling
        position = math.ceil(len(items) / 2)
        first_list = items[:position]
        second_list = items[position:]
        return [first_list, second_list]




if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
