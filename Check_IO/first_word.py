
def first_word(str):
    #using built in to replace then split to list
    str = str.replace(',', ' ').replace('.', ' ').split()
    return(str[0])

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    assert first_word("Hello.world") == "Hello"

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
