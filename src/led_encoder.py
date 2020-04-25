def chars_to_binary(chars):
    """
    takes in a 7 bit string of abcdefg
    where lower is off, upper is on
    and returns the binary representation
    of that code

     |  a  |
     |f   d|
     |  g  |
     |e   c|
     |  d  |

    """
    enc_string = ''
    for char in chars:
        if char.isupper():
            enc_string += '1'
        else:
            enc_string += '0'

    return enc_string

def encode(string):
    enc_string = chars_to_binary(string)
    return int('0' + ''.join(reversed(enc_string)), base=2)


def custom_char(char):
    """
    Turns lower case characters into raw LED
    mappings where possible
    """
    if char =='a':
        return encode('abcDefg') # TODO
    elif char == 'b':
        return encode('abCDEFG')
    elif char == 'c':
        return encode('abCDEfg')
    elif char == 'd':
        return encode('aBCDEfG')
    elif char == 'e':
        return encode('abcDefg') # TODO
    elif char == 'f':
        return encode('abcDefg') # TODO
    elif char == 'g':
        return encode('ABCDeFG')
    elif char == 'h':
        return encode('abCdEFG')
    elif char == 'i':
        return encode('abCdefg')
    elif char == 'j':
        return encode('abcDefg') # TODO
    elif char == 'k':
        return encode('abcDefg') # TODO
    elif char == 'l':
        return encode('abcDefg') # TODO
    elif char == 'm':
        return encode('abcDefg') # TODO
    elif char == 'n':
        return encode('ABCdEFg')
    elif char == 'o':
        return encode('abcDefg') # TODO
    elif char == 'p':
        return encode('ABcdEFG')
    elif char == 'q':
        return encode('abcDefg') # TODO
    elif char == 'r':
        return encode('abcdEfG')
    elif char == 's':
        return encode('abcDefg') # TODO
    elif char == 't':
        return encode('abcDEFG')
    elif char == 'u':
        return encode('abCDEfg')
    elif char == 'v':
        return encode('abcDefg') # TODO
    elif char == 'w':
        return encode('abcDefg') # TODO
    elif char == 'x':
        return encode('abcDefg') # TODO
    elif char == 'y':
        return encode('abcDefg') # TODO
    elif char == 'z':
        return encode('abcDefg') # TODO
    elif char == '1':
        return encode('abcDefg') # TODO
    elif char == '2':
        return encode('abcDefg') # TODO
    elif char == '3':
        return encode('abcDefg') # TODO
    elif char == '4':
        return encode('abcDefg') # TODO
    elif char == '5':
        return encode('abcDefg') # TODO
    elif char == '6':
        return encode('abcDefg') # TODO
    elif char == '7':
        return encode('abcDefg') # TODO
    elif char == '8':
        return encode('abcDefg') # TODO
    elif char == '9':
        return encode('abcDefg') # TODO
    elif char == '0':
        return encode('abcDefg') # TODO
    else:
        return encode('abcDefg') # TODO