file = input("Enter file name: ")
fhand = open(file)

words = dict()

for line in fhand:
    words_list = line.split()
    for i in range(len(words_list)):
        words[words_list[i]] = 0

print("mind-numbing" in words)
print("lol" in words)
print("hardware" in words)
