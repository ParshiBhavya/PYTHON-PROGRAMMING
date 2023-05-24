class human:
    x=5

h1=human()
print(h1.x)

class man:
    def __init__(self,name,age):
        self.name=name
        self.age=age

h1=man("bhavya",20)
print(h1.name)
print(h1.age)

class me:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def methods(self):
        print("my name is "+ self.name)
        print("my age is "+ self.age)
h1=me("bhavya","20")
h1.methods()
h2=me("Divya","15")
h2.methods()