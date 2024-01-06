fname = input("Enter a file name: ")
fhand = open(fname)

mail_day_freq = dict()

for line in fhand:
    if line.startswith("From:"):
        continue
    
    elif line.startswith("From"):
        email_line = line.split()
        mail_day_freq[email_line[2]] = mail_day_freq.get(email_line[2],0) + 1

print(mail_day_freq)



