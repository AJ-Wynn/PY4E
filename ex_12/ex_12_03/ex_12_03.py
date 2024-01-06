import re
fname = input("Enter file:")
fhand = open(fname)

numtotal = list()

for line in fhand:
    line = line.rstrip()
    numlist = re.findall("[0-9]+", line)

    for i in range(len(numlist)):
        numtotal.append(int(numlist[i]))
    

print(sum(numtotal))

 
    



    

    
                     

