import re
def credit_check(card: str):

if __name__ == '__main__':
    print("Checks:")
    assert credit_check(4123456789123456) == "Valid"
    assert credit_check(5123-4567-8912-3456) == "Valid"
    assert credit_check(61234-567-8912-3456) == "Invalid"