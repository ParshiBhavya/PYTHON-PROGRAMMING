n=int(input('Enter no of elements required in list:'))
data=[]
for i in range(n):
      data.append(int(input()))
      
sum=0
for d in data:
    sum=sum+d

print('sum is:',sum)
print('Avg is',int(sum/len(data)))
