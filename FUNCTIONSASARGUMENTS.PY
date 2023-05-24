list=[' swetha',' bhavya',' pavani']
list1=[" ",]
def loop(list):
    print(list*3)
loop(list)

def simple(crazy,list):
  for items in list:
      crazy(items)

simple(loop,list)

print(type(list1))
