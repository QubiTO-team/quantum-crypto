def decode(cipher, bit_position_probs, K_zero_prob, K_one_prob, dec_bits):
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
    return dec_text
