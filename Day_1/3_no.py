#Count vowels in a string 

word = input("Enter a string:  ")
count = 0

for i in range(len(word)):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        count += 1

print("The numebr of vowels in the string are: ", count)