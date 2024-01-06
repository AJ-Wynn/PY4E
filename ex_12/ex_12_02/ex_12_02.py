import re
fname = input("Enter file:")
fhand = open(fname)

counter = 0
sum = 0

for line in fhand:
    line = line.rstrip()
    num = re.findall("^New Revision: ([0-9]+)",line)
    
    if len(num) != 1:
        continue
    counter = counter + 1
    fnum = float(num[0])
    sum = sum + fnum

print(int(sum / counter))



    

    
                     

