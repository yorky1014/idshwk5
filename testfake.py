f1=open("test.txt","r")

f2=open("result.txt","w")

for line in f1:

    if line == "" or line.startswith("#"):

        continue

    line = line.strip()

    if len(line)>20:

        f2.write(line)

        f2.write(",")

        f2.write("dga\n")        

        continue

    amount = 0

    for letter in line:

        if 48 <= ord(letter) <= 57:

            amount = amount+1

    threshold = len(line)*0.1

    if amount >= threshold:

        f2.write(line)

        f2.write(",")

        f2.write("dga\n")

        continue

    f2.write(line)

    f2.write(",")

    f2.write("nodga\n")

f1.close()

f2.close()
