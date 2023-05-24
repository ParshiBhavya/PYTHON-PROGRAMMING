tuple1=("me","mom","dad")
myit=iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))

strings="apples"
myit=iter(strings)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class mynumbers:
    def __iter__(self):
     self.a=1
     return self
    def __next__(self):
     x=self.a
     self.a+=1
     return x

myclass=mynumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

