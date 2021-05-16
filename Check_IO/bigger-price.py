"""
You have a table with all available goods in the store. The data is represented as a list of dicts
Your mission here is to find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one
Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument.
"""
#Import pretty print
"""
#This is me working through how to sort list of dics
from pprint import pprint
mylist = [
    {
        'model':'f250',
        'brand':'ford',
        'price':2020
    },
    {
        'model':'zx2',
        'brand':'ford',
        'price':2001
    }
]

mylist.append(
    {
        'model':'3',
        'brand':'mazda',
        'price':2015
    })

pprint("This is mylist unsorted")
pprint(mylist)
print("Sorted list")
#Stole from online, but the key becomes the function of lambda, which gets the price
mylist.sort(reverse=True, key=lambda item: item['price'])
pprint(mylist)

#Output only what I want
print("Pieces")
pprint(mylist[0:])
"""
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    data.sort(reverse=True, key=lambda item: item['price'])
    return data[0:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
