import random

# The original plaintext message we want to encrypt and then attempt to decrypt.
m = """here is a long stretch of english text intended to test your decryption algorithm. the science of cryptanalysis is built on the fact that language is not random. in standard english, the letter e is overwhelmingly common, appearing more often than any other character. conversely, letters like z and q are incredibly rare. when you use a biased key, you leak information because the ciphertext preserves some of the statistical structure of the original message.
imagine you are encrypting this very paragraph. if your key is biased towards one, it will flip the bits of this message more often than not. this creates a noisy channel. your task is to look at the noisy output and ask yourself which original character best explains what you see. for example, the space character appears frequently between words. in binary, a space is number thirty-two. this particular bit pattern is very distinct from a lowercase letter.
by combining the known frequency of letters with the known bias of your key, you can reconstruct the text. it might not be perfect. you might see typos or strange glitches where the probability was too close to call. however, if the text is long enough, the words should be readable. good luck with your experiment."""

# ==========================================
# 1. TEXT TO BINARY CONVERSION
# ==========================================
# We convert each character in the string 'm' to its ASCII integer value using ord(),
# then format it as a 7-bit binary string (e.g., 'a' becomes '1100001').
# We join all these 7-bit chunks together into one long string of 0s and 1s.
bit_m = "".join(f"{ord(char):07b}" for char in m)

# ==========================================
# 2. BIASED KEY GENERATION
# ==========================================
# A perfectly secure One-Time Pad requires a completely random key (50% zeros, 50% ones).
# Here, we intentionally create a flawed, biased key to demonstrate cryptanalysis.
K_one_prob = 0.97         # The key will consist of about 97% ones.
K_zero_prob = 1 - K_one_prob # The key will consist of about 3% zeros.

# Generate the key: For every bit in our message, generate a '1' 97% of the time, and a '0' 3% of the time.
key = "".join("1" if random.random() < K_one_prob else "0" for _ in range(len(bit_m)))

# ==========================================
# 3. XOR ENCRYPTION / DECRYPTION
# ==========================================
# This function performs a bitwise XOR (exclusive OR) between the text bits and the key bits.
# In XOR: 0^0=0, 1^1=0, 1^0=1, 0^1=1. 
# It effectively flips the message bit if the key bit is 1, and leaves it alone if the key bit is 0.
def xor_strings(text_bits, key_bits):
    return "".join(str(int(b1) ^ int(b2)) for b1, b2 in zip(text_bits, key_bits))

# Encrypt the binary message using our biased key.
cipher = xor_strings(bit_m, key)

# ==========================================
# 4. ENGLISH CHARACTER PROBABILITIES
# ==========================================
# This dictionary maps characters to their approximate frequency in standard English.
# Because English is predictable (e.g., 'e' and ' ' are very common), the resulting binary
# representation of English text is also predictable, which we exploit below.
char_probs = {
    ' ': 0.18288, 'e': 0.10267, 't': 0.07517, 'a': 0.06532, 'o': 0.06159,
    'n': 0.05712, 'i': 0.05668, 's': 0.05317, 'r': 0.04988, 'h': 0.04978,
    'l': 0.03317, 'd': 0.03283, 'u': 0.02276, 'c': 0.02234, 'm': 0.02027,
    'f': 0.01983, 'w': 0.01704, 'g': 0.01625, 'p': 0.01504, 'y': 0.01428,
    'b': 0.01259, 'v': 0.00796, 'k': 0.00561, 'x': 0.00141, 'j': 0.00098,
    'q': 0.00084, 'z': 0.00051, '.': 0.0060,  ',': 0.0060,  '\'': 0.0020,
    '"': 0.0020,  '-': 0.0010,  '?': 0.0005,  '\n': 0.0005
}

# ==========================================
# 5. PRE-CALCULATING BIT DISTRIBUTIONS
# ==========================================
# Instead of calculating the probability of a bit being 0 or 1 on the fly, 
# we calculate it once for all 7 positions of an ASCII character.
# bit_position_probs[i]['0'] will store the total probability that the i-th bit of an English character is '0'.
bit_position_probs = [{'0': 0.0, '1': 0.0} for _ in range(7)]

for char, prob in char_probs.items():
    bits = f"{ord(char):07b}" # Convert character to 7-bit binary
    for i in range(7):
        # Add the character's overall frequency to the specific bit's probability pool
        bit_position_probs[i][bits[i]] += prob

# ==========================================
# 6. BAYESIAN CRYPTANALYSIS (THE DECRYPTION)
# ==========================================
# We will look at each bit of the ciphertext and guess what the original bit was.
dec_bits = ""
for l, c_bit in enumerate(cipher):
    i = l % 7 # Determine which of the 7 bit positions we are currently analyzing
    
    # Get the prior probability that this specific bit position is a 0 or a 1 in standard English
    p_m0 = bit_position_probs[i]['0']
    p_m1 = bit_position_probs[i]['1']
    
    # We apply the numerator of Bayes' Theorem: P(Message | Cipher) is proportional to P(Cipher | Message) * P(Message)
    # We want to find out which scenario is heavier (has a higher weight).
    if c_bit == "0":
        # If the ciphertext is 0, it came from either:
        # 1. Original bit was 0 AND Key was 0 (0^0 = 0)
        weight_m0 = p_m0 * K_zero_prob
        # 2. Original bit was 1 AND Key was 1 (1^1 = 0)
        weight_m1 = p_m1 * K_one_prob
    else: # c_bit == "1"
        # If the ciphertext is 1, it came from either:
        # 1. Original bit was 0 AND Key was 1 (0^1 = 1)
        weight_m0 = p_m0 * K_one_prob
        # 2. Original bit was 1 AND Key was 0 (1^0 = 1)
        weight_m1 = p_m1 * K_zero_prob
        
    # Make our best guess based on which calculated weight is higher
    dec_bits += "0" if weight_m0 > weight_m1 else "1"

# ==========================================
# 7. CONVERTING BITS BACK TO TEXT
# ==========================================
# Group the decrypted bits back into chunks of 7, convert from base-2 binary to an integer,
# and finally convert that integer back into an ASCII character.
dec_text = "".join(chr(int(dec_bits[i:i+7], 2)) for i in range(0, len(dec_bits), 7))

print("ANALYZED TEXT:\n" + dec_text)

# ==========================================
# 8. ACCURACY CALCULATION
# ==========================================
# Compares the original message to our Bayesian decryption to see how well the algorithm performed.
def calculate_accuracy(original, decrypted):
    min_len = min(len(original), len(decrypted))
    if min_len == 0: return 0
    correct = sum(1 for i in range(min_len) if original[i] == decrypted[i])
    return correct / len(original)

accuracy = calculate_accuracy(m, dec_text)
print(f"\nAccuracy: {accuracy:.2%}")