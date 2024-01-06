fname = input("Enter a file name: ")
fhand = open(fname)

msg_count = dict()

for line in fhand:
    if line.startswith("From:"):
        continue
    
    elif line.startswith("From"):
        list = line.split()
        sender = list[1]
        msg_count[sender] = msg_count.get(sender, 0) + 1

largest = None
lsender = None
for email in msg_count:
    if largest is None or msg_count[email] > largest:
        largest = msg_count[email]
        lsender = email

print(lsender, largest)


        
    
    
    
    

