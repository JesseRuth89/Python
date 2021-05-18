import re
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    decode = ""
    first_check = True
    for x in code.split(" "):
        if (MORSE.get(x)) is None:
            decode = decode + " "
            continue
        else:
            if code.split()[0] == x and (MORSE.get(x)).isalpha() and first_check:
                first_check = False
                decode = decode + (MORSE.get(x)).upper()
            else:
                decode = decode + (MORSE.get(x))
    return(re.sub(' +',' ',decode))


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print(morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----"))
    print("Coding complete? Click 'Check' to earn cool rewards!")
