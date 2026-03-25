import time

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Function used to encrypt a plaintext using Caesar's Cipher given a certain key k

def encrypt_Caesar(in_f, out_f, k):
    ciphred = ''
    for line in in_f:
        for char in line:
            upper_char = char.upper()
            if upper_char in alphabet:
                ciphred+= alphabet[(alphabet.index(upper_char)+k)%26]
            else:
                ciphred += char
    print(ciphred, file= out_f)
    return  

#Function used to decrypt a ciphertext encrypted with Caesar's Cipher given a certain key k

def decrypt_Caesar(in_f, out_f, k):
    deciphred = ''
    for line in in_f:
        for char in line:
            upper_char = char.upper()
            if upper_char in alphabet:
                deciphred += alphabet[(alphabet.index(upper_char) - k) % 26]
            else:
                deciphred += char
    print(deciphred, file=out_f)
    return    

#Function used to brute-force Caesar's Cipher: tries all of the 26 different possible encryptions
#input_name is the name of the file containing the ciphertext, output_name is the name of the file where the result of the brute-force attack will be printed

def brute_force_Caesar(input_name, output_name): 

    out_f = open(output_name, 'w')
    out_f.close()
    
    in_f = open(input_name, 'r')
    out_f = open(output_name, 'a')
    start = time.perf_counter()
    
    for key in range(26):
        print(f'Key = {key+1}', file=out_f)
        in_f.seek(0) 
        decrypt_Caesar.decrypt_Caesar(in_f, out_f, key)
        print('\n', file=out_f)

    end = time.perf_counter()
    print(f"Total Execution Time for Brute Force: {end-start}", file=out_f)
    in_f.close()
    out_f.close()
    return


    
