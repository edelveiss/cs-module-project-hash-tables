#cd histo  -> python3 histo.py
'''
Hints:
Items: .items() method on a dictionary might be useful.
Sorting: it's possible for .sort() to sort on multiple keys at once.
Sorting: negatives might help where reverse won't.
Printing: you can print a variable field width in an f-string with nested braces, like so {x:{y}}

'''
def print_dict(d_dict):
    for key, values in d_dict.items():
        print("key: ", key, " ----values-->>: ",values)

# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()

data_dict = {}
words_list = words.lower().split()

for i in range(len(words_list)):
    word_without_chars = words_list[i].strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
    if word_without_chars not in data_dict:
        data_dict[word_without_chars] = 1
    else:
        data_dict[word_without_chars] += 1


sorted_data_counter = sorted(data_dict.items(), key=lambda x: x[1], reverse=True) #got an array of tuples

#Print a histogram showing the word count for each word
for i in sorted_data_counter:
    print(i[0] + ' '*(20 - len(i[0])) + '#'*i[1])
	