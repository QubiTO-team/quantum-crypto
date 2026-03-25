import random 

def random_key(length) of equal length. 
    # Creates a random binary key for encoding.
    # Input: length (int)
    # Output: result (binary string)
    result = ""
    for _ in range(length):
        result += str(random.choices([1,0],[0.5,0.5])[0])
    return result

def binary_to_str(binary):
    # Converts python binary format into a binary string.
    res = ""
    padding = 9 - len(binary)
    for _ in range(padding):
        res += '0'
    res += binary[0] + binary[2:]
    return res

def binary_text(text):
    # Converts a full text of arbitrary length into a binary string.
    binary = ""
    for char in text:
        binary += binary_to_str(bin(ord(char)))
    return binary

def ascii_text(text):
    # Converts a binary string of arbitrary length into an ascii string.
    ascii = ""
    for i in range(len(text) // 8):
        one_char = text[i * 8:(i + 1) * 8]
        ascii += chr(int(one_char, 2))
    return ascii

def xor(text, key):
    # Performs XOR on two binary strings of equal length. 
    result = ""

    if len(text) != len(key):
        print("Key lengths must match!")
        return -1
    
    for i in range(len(text)):
        result += str(int(key[i]) ^ int(text[i]))
    return result
