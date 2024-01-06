fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    #print('Debug:', words)

    for i in range(len(words)):
        if words[i] == 'Mon' or words[i] == 'Tue' or words[i] == 'Wed' or words[i] == 'Thu' or words[i] == 'Fri' or words[i] == 'Sat' or words[i] == 'Sun' :
            print(words[i])
    
    