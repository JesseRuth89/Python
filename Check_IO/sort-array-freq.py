"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
the number of times they appear in elements. If two elements have the same frequency,
they should end up in the same order as the first appearance in the iterable
"""


def frequency_sort(items):
    # sorting list by the count of individual item
    # pretty easy to read
    f1 = sorted(items, key=items.count, reverse=True)
    print(f1)
    for i in f1:
        print(f' {i} x {f1.index(i)} ', end=":")
    # sorting the sorted list using a function of the index position
    # The index() method only returns the first occurrence of the value.
    print()
    return sorted(f1, key=lambda d: (f1.index(d)), reverse=False)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    #assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    #assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    #assert list(frequency_sort([])) == []
    #assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
