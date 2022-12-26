x=int(input('enter any number'))
n=x
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
    
print('rev of number is:',rev)

if(rev==x):
    print(x,'palindrome')
else:
    print(x,'not a palindrome')
