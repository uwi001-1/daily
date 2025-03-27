#Check if the last letter of each word in a sentence overlaps with the first letter of the next word

def check_overlap(sentence):
    sen = sentence.lower()
    for i in range(len(sen)):
        if sen[i] == " ":
            if sen[i-1] == sen[i+1]:
                sidd = True
            else:
                return False
    if sidd:
        return True

sentence = input("Enter the sentence:  ") #She eats strawberries
print(check_overlap(sentence))