from binascii import unhexlify, hexlify, b2a_base64, a2b_hex, b2a_hex
from operator import xor 
from collections import Counter

# http://cryptopals.com/sets/1
def hex_to_base64(input, test = False):
    decoded = unhexlify(input)
    encoded = b2a_base64(decoded)
    if test:
        print(encoded)
    return(encoded)

# http://cryptopals.com/sets/1/challenges/2
def logical_xor(a, b):
    result = hex(int(a, 16) ^ int(b,16))
    # string representation
    return result[2:]
print(logical_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))

def xor_cipher(input):
    # determines size chunks that the input dict is split into
    split_into = 1
    multi_char = [input[i:i+split_into] for i in range(0, len(input), split_into)]
    multi_dict = dict(Counter(multi_char))
    print(multi_dict)
    new_message = ""
    # for key,value in multi_dict.items():
        # print("key " + str(key))
        # print(unhexlify(logical_xor(input, key)))
    for item in input:
        new_message += logical_xor(item, "9")
    print(new_message)
    print(unhexlify(new_message))
        

# xor_cipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
print(int("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 16))