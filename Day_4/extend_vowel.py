#Extend the vowels in a string

def extend_vowels(word, n):
    new_string = ""
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or  word[i] == "i" or  word[i] == "o" or  word[i] == "u":
            new_string = new_string + word[i]*n
        else:
            new_string = new_string + word[i]
    return new_string

word = input("Enter the word:  ").lower()
num = int(input("Enter the numebr of times to increase vowels:  "))
print(extend_vowels(word, num))