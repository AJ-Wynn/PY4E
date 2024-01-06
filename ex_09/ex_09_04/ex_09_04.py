sfile = input("Enter file :")
fhand = open(sfile)

unq_words = list()
for line in fhand:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in unq_words:
            unq_words.append(words[i])

unq_words.sort()
print(unq_words)
