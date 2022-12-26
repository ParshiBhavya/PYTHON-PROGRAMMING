n=int(input('enter no of elements required in list:'))
data=[]
for i in range(n):
  data.append(int(input()))
temp=data[0]
for d in data:
    if(d<temp):
     temp=d
print("smallest=",temp)
