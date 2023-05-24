n = int(input("Enter total number of names:"))

Name = []

print("\n Enter names: ")

for i in range(0, n):
    x = input()
    Name.append(x)

print("\n Names are:")

for i in range(0, n):
    mylist = (Name[i].capitalize())
    print(list(mylist.split(',')))

n = int(input("Enter total number of names:"))

mynames = []

print("\n Enter names: ")

for i in range(0, n):
    x = input()
    mynames.append(x)

print("\n Names are:")

for i in range(0, n):
    mylist = (mynames[i].capitalize())
    print(list(mylist.split(',')))