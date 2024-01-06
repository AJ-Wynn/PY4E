file = input("Enter a file name: ")
fhand = open(file)

counter = 0
for line in fhand:
    if line.startswith("From:"):
        continue
    
    elif line.startswith("From"):
        counter = counter + 1
        email_line = line.split()
        print(email_line[1])

print("There were %d lines in the file with From as the first word" % (counter))