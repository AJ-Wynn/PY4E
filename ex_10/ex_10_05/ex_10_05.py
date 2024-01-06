fname = input("Enter a file name: ")
fhand = open(fname)

domain_count = dict()

for line in fhand:
    if line.startswith("From:"):
        continue
    
    elif line.startswith("From"):
        list = line.split()
        sender = list[1]
        at_index = sender.find("@")
        domain = sender[at_index + 1:]

        domain_count[domain] = domain_count.get(domain, 0) + 1


print(domain_count)

        
    
    
    
    

