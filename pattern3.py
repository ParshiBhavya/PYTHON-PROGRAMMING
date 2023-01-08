n=int(input('enter any number:'))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print('*',end=' ')
    print()
