"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

    The initial and final markers are always different.
    If there is no initial marker, then the first character should be considered the beginning of a string.
    If there is no final marker, then the last character should be considered the ending of a string.
    If the initial and final markers are missing then simply return the whole string.
    If the final marker comes before the initial marker, then return an empty string.
"""



def between_markers(text: str, begin: str, end: str):
    #print(len(start))
    #print(string.find(start))
    if text.find(begin) == -1:
        startp = 0
    else:
        startp = text.find(begin) + len(begin)

    if text.find(end) == -1:
        endp = len(text) + 1
    else:
        endp = text.find(end)

    if startp >= endp:
        return('')
    else:
        return(text[startp:endp])



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
