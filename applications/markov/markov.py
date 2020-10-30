#cd markov  -> python3 markov.py
import random
import sys

def print_dict(d_dict):
    for key, values in d_dict.items():
        print("key: ", key, " ----values-->>: ",values)

def random_sentence(data_dict, start_words, end_words):
    random_word = random.choice(list(start_words))
    first_word = random_word
    stop = False
    while not stop:
        print(random_word, end = ' ')
        if random_word in end_words:
            stop = True
            #Stretch Goal
            #there is always a close quote for an opening quote in the sentence.
            if first_word[0] == '"' and random_word[-1] != '"':
                sys.stdout.write('\b')
                print('"')
        following_the_random_word = data_dict[random_word]
        random_word = random.choice(list(following_the_random_word))
        

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
#-----------------------------------------------

data_dict = {}
words_list = words.split()

for i in range(len(words_list)-1):
    if words_list[i] not in data_dict:
        data_set = set()
        data_dict[words_list[i]] = data_set
        data_set.add(words_list[i+1])
    else:
        data_dict[words_list[i]].add(words_list[i+1])

        
start_words = set()
for key in data_dict.keys():
    if key[0] == '"' and key[1].isupper() or  len(key) > 1 and key[0].isupper():
        start_words.add(key)

end_words = set()
for key in data_dict.keys():
    if key[-1] == '.' or key[-1] == '!' or key[-1] == '?' or (key[-1] == '"' and (key[-2] == '.' or key[-2] == '!' or key[-2] == '?')):
        end_words.add(key)

# test_str = "Cats and dogs and birds and fish dogs birds"
# print_dict(data_dict)

# construct 5 random sentences
for i in range(5):
    random_sentence(data_dict,start_words, end_words)

