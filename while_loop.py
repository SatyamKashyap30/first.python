# count = 1 
# while count <= 5:
#     print(count)
#     count += 1

# count = 1
# while count <= 10:
#     print(count)
#     count += 1

# count = 5 #(count start)
# while count >= 1:#(count end)
#     print(count)
#     count -= 1

# count = 10
# while count >= 4:
#     print(count)
#     count -= 1

# i = 1
# while i <= 5:
#     print("shivam")
#     i += 1

# i = 0
# while i <= 10:
#     print(i)
#     i += 2

# x = 1
# while x <= 10:
#     print(x)
#     x += 2
 
# x = 3
# while x <= 30:
#     print(x)
#     x += 3

# s = 1
# while s <= 5:
#     print(s,s*s)
#     s += 1

# i = 1
# total = 0
# while i <= 10:
#     total = total + i
#     i = i + 1
# print("sum=",total)

# n = 9
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i = i + 1



# n = 5
# fact = 1
# while n > 0:
#     fact = fact * n
#     n = n - 1
# print("factorial=", fact)


# n = 2
# fact = 5 
# while n > 0:
#     fact = fact * n
#     n = n - 1
# print("factorial=", fact)


# n = 10
# fact = 3
# while n > 0:
#     fact = fact * n
#     n = n - 1
# print("factorial=", fact)

# n = 11
# i = 1
# while i <= 10:
#     print(n,"x",i,"=",n*i)
#     i = i + 1

# s = (23,45,47,66,78)
# print(s)
# print(type(s))

# student = ("suraj","shivam","adarsh","shubham","vaibhav")
# print(student)
# print(type(student))
# print(student[0])
# print(student[4])

# tup = (10,20,30,40,50)
# print(tup[2])

# fruits = ("apple","banana","grapes","mango","gauvae")
# print(fruits[-5:-1])

# tup = (5,
#        "shivam",
#        56.89,
#        True)

# print(tup)

# t = (10,20,30,40,50)
# print(t[3])

# t = ("Red","Green","Blue","Yellow")
# print(t[-4])

# t = (5,10,15,20,25,30)
# print(t[-2])

# t = ("A","B","C","D","E")
# print(t[0])
# print(t[2])
# print(t[4])

# t = (100,200,300,400,500)
# print(t[1]+t[3])

import random
choices = ["rock","paper","scissors"]

user = input("Eneter rock,paper,or scissors:").lower()
computer = random.choice(choices)

print("Computer chose:",computer)

if user not in choices:
    print("invalid choices!")
elif user == computer:
    print("it's a draw!")
elif(user == "rock" and computer =="scissors")or\
    (user == "paper" and computer == "rock") or\
    (user == "scissors" and computer == "paper"):
    print("you win!")
else:
    print("computer wins!")