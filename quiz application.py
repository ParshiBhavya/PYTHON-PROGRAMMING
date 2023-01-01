name=input('enter your name:')
score=0
print("Hi",name,",welcome to the quiz!")
print('Q1.What is the capital of M.P?')
print("1.kolkata 2.hyderabad 3.Bhopal")
ans=int(input('Enter your choice:'))
if(ans==3):
    score=score+20
    print('correct Answer,with score=',score)
else:
    print('wrong answer,with score',score)

print('Q1.What is the capital of A.P?')
print("1.Amaravathi 2.hyderabad 3.Bhopal")
ans=int(input('Enter your choice:'))
if(ans==1):
    score=score+20
    print('correct Answer,with score=',score)
else:
    print('wrong answer,with score',score)

print('Q1.What is the capital of Telangana?')
print("1.Amaravathi 2.hyderabad 3.Bhopal")
ans=int(input('Enter your choice:'))
if(ans==2):
    score=score+20
    print('correct Answer,with score=',score)
else:
    print('wrong answer,with score',score)


if(score>=40):
    print('congratulations,you passed with score,',score)
else:
    print('sorry,you got only',score)

input()
    
    

