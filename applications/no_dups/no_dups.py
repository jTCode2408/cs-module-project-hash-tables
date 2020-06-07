def no_dups(s):
    # Your code here
    s = s.split()
    dict={}
    no_dupe = []

    for i in s:
        if i not in dict:
            dict[i] = 1
            no_dupe.append(i)
    return ' '.join(no_dupe)
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))