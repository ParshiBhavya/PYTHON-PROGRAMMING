def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def power(a,b):
    ans=1
    for i in range(1,b+1):
        ans=ans*a
    return ans 
