
def word_count(s):
    counter_dict = {}
    data = s.lower().split()
    for word in data:
        word_without_chars = word.strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
        if word_without_chars == "":
            return {}
        if word_without_chars in counter_dict:
            counter_dict[word_without_chars] += 1
        else:
            counter_dict[word_without_chars] = 1

    
    return counter_dict

    



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))