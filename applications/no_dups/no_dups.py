def no_dups(s):
    accumulator_str = ""
    set_str = set() #O(s)
    split_str = s.split()

    for word in split_str: #O(len(split_str))
        if word not in set_str: #O(1)
            set_str.add(word)
            accumulator_str += word + " "

    return accumulator_str.strip() #O(s)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))