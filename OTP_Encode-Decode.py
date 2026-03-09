import random 

SuperSecretText = input("What would you like to encode and decode?");
def random_key(length):
    result = ""
    for _ in range(length):
        result += str(random.choices([1,0],[0.5,0.5])[0])
    return result

def binary_to_str(binary):
    res = ""
    padding = 9 - len(binary)
    for _ in range(padding):
        res += '0'
    res += binary[0] + binary[2:]
    return res

def binary_text(text):
    binary = ""
    for char in text:
        binary += binary_to_str(bin(ord(char)))
    return binary
def ascii_text(text):
    ascii = ""
    for i in range(len(text) // 8):
        one_char = text[i * 8:(i + 1) * 8]
        ascii += chr(int(one_char, 2))
    return ascii
def xor(text, key):
    result = ""

    if len(text) != len(key):
        print("Key lengths must match!")
        return -1
    
    for i in range(len(text)):
        result += str(int(key[i]) ^ int(text[i]))
    return result

key = random_key(len(SuperSecretText) * 8)
print(str.center("Original Text:", 30), SuperSecretText)
print(str.center("Random Key:",30),key)
binary = binary_text( SuperSecretText)
print(str.center("Text converted to binary:",30),binary)

EncodedSuperSecretText = xor(binary, key)
print(str.center("Encoded binary text:", 30), EncodedSuperSecretText)
DecodedSuperSecretText = xor(EncodedSuperSecretText, key)
print(str.center("Decoded binary text:",30), DecodedSuperSecretText)
print(str.center("Recovered text:", 30), ascii_text(DecodedSuperSecretText))
