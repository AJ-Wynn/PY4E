fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    
    else:
        print("File cannot be opened:", fname)
        exit()

count = 0
total = 0
for line in fhand:
    if not "X-DSPAM-Confidence:" in line:
        continue
    line = line.rstrip()
    value = line[line.find(":")+2:]
    fvalue = float(value)
    count = count + 1
    total = total + fvalue

avg = total / count
print ("Average spam condfidence: ",avg)


