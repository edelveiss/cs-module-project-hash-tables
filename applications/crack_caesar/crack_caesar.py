#cd crack_caesar  -> python3 crack_caesar.py
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

import collections

encode_arr = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

#---------encode function---------------------
def encode(plain_text,encode_table):
    cipher = "" #text accumulator
    for char in plain_text:
        if char.isalpha():
            cipher += encode_table[char]
        else:
            cipher += char
    return cipher

#---------decode function---------------------
def decode(cipher_text,decode_table):
    plain_text = "" #text accumulator
    for char in cipher_text:
        if char.isalpha():
            plain_text += decode_table[char]
        else:
            plain_text += char
    return plain_text

#-----------print dictionary function----------------
def print_dict(d_dict):
    for key, values in d_dict.items():
        print("key: ", key, " ----values-->>: ",values)

# Read in all the words in one 
with open("ciphertext.txt") as f:
    words = f.read()

# dictionary for key:letters and value: letter_counters
data_dict = {}

for i in range(len(words)):
    if words[i].isalpha() and words[i] not in data_dict:
        data_dict[words[i]] = 1
    elif words[i].isalpha() and words[i]  in data_dict:
        data_dict[words[i]] += 1


sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True) 
sorted_dict = collections.OrderedDict(sorted_data)

sorted_arr = []
# transformation dictionary to a list
def getList(dict):   
    return [*dict] 
sorted_arr = getList(sorted_dict)


encode_table ={}
for i in range(len(sorted_arr)):
    encode_table[encode_arr[i]] = sorted_arr[i]


decode_table = {}
for key, value in encode_table.items():
    decode_table[value] = key

# decode text
reversed_plain_text = decode(words,decode_table)
print(reversed_plain_text) 

# encode text
# cipher = encode(words,encode_table)
# print(cipher)




