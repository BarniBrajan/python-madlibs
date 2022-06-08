sentences = ["We all are ", "You can do more than you ", "Life is "]
words = []
print("Insert 3 worlds: ", end =" ")

for i in range(3):
    words.append(input()) 

for i in range(3):
    print(sentences[i] + words[i])

