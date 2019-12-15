import csv
import random

data = {
    "passwords":[],
    "cc_numbers":[]
}
print("Getting password values")
#get the passwords
passwords = []
with open('pwd.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        data["passwords"].append([row[0]])

print("Generating CC values")
#generate some cc numbers
for i in range(0, 500000):
    cc_number = [str(random.randint(0,9)) for _ in range(16)]
    cc_cvv = [str(random.randint(0,9)) for _ in range(16)]
    cc_exp = [str(random.randint(0,9)) for _ in range(4)]

    cc = "".join(cc_number) + "/" + "".join(cc_cvv) + "/" + "".join(cc_exp)
    data["cc_numbers"].append([cc])

print("Final randomization and save")
final_data = []
for key in data.keys():
    print("Adding " + key + " size:" + str(len(data[key])))
    for i in data[key]:
        final_data.append(i)
random.shuffle(final_data)

with open('exfiltration_data.csv', 'wb') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(final_data)