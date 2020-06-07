import re

def word_count(s):
    # Your code here
    dict = {}
    for word in re.sub(r"[^a-zA-Z ']", ' ', s).lower().split():
        if word in dict:
            dict[word] +=1
        else:
            dict[word] =1
    return dict




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))