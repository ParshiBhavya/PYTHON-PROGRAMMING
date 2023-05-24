x=lambda a,b:a+b
print(x(22,18))

def f1(n):
    return lambda a:a*n
doub=f1(2)
print(doub(11))

def prime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

filtered=filter(prime,range(10))
print("The values are:",list(filtered))

def square(x):
        return x*x
numbers=[1,3,5,7,9]
listofsquares=map(square,numbers)
print("The squares are:",list(listofsquares))
