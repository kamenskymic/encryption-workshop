from typing import Final

CAPITAL_LETTER: Final = 1
LOWERCASE_LETTER: Final = -1
MOST_FREQUENT_LETTER: Final = 'E'


def break_shift_cipher():
    ciphertext_string = input("Enter string: ")
    frequency = {}
    find_frequency(ciphertext_string, frequency)
    max_frequency = max(frequency, key = frequency.get)
    shift = ord(max_frequency)-ord(MOST_FREQUENT_LETTER)
    print("The original message is: ")
    return (shift_dec(ciphertext_string, shift))
    

def find_frequency(ciphertext_string, frequency):
    for char in ciphertext_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1


def shift_enc(plaintext_string, shift):
    encrypted_string=""
    for char in plaintext_string:
        if(ord(char)==ord("3") or ord(char)==ord(" ")):
            encrypted_string+=(char)
            continue
        if((ord(char)>ord("z"))or(ord(char)<ord("A"))):
            print("Faulty input")
            return
        if(capital_or_lowercase(char) == CAPITAL_LETTER):
            if(((ord(char))+shift)>(ord("Z"))):
                encrypted_string+=(chr(((ord("A"))+(((ord(char))+shift)-(ord("Z")))-1)))
                continue
        if(capital_or_lowercase(char) == LOWERCASE_LETTER):
            if(((ord(char))+shift)>(ord("z"))):
                encrypted_string+=(chr(((ord("a"))+(((ord(char))+shift)-(ord("z")))-1)))
                continue
        encrypted_string+=(chr((ord(char))+shift))
    return encrypted_string


def shift_dec(ciphertext_string, shift):
    original_string=""
    for char in ciphertext_string:
        if(ord(char)==ord("3") or ord(char)==ord(" ")):
            original_string+=(char)
            continue
        capital_or_lowercase(char)
        if((ord(char)>ord("z"))or(ord(char)<ord("A"))):
            print("Faulty input")
            return
        if(capital_or_lowercase(char) == CAPITAL_LETTER):
            if(((ord(char))-shift)<(ord("A"))):
                original_string+=(chr(ord("Z")+(ord(char)-shift-ord("A"))+1))
                continue
        if(capital_or_lowercase(char) == LOWERCASE_LETTER):
            if(((ord(char))-shift)<(ord("a"))):
                original_string+=(chr(ord("z")+(ord(char)-shift-ord("a"))+1))
                continue
        original_string+=(chr((ord(char))-shift))
    return original_string

def capital_or_lowercase(char):
    if(ord(char)>=ord("A"))and(ord(char)<=ord("Z")):
        return CAPITAL_LETTER
    elif(ord(char)>=ord("a"))and(ord(char)<=ord("z")):
        return LOWERCASE_LETTER


print(break_shift_cipher())
