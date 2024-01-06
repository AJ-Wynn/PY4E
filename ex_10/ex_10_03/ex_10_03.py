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

print(msg_count)
