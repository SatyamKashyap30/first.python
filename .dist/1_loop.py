#Range()
seq = range(5)

for i in seq:
    print(i)


for i in range(10):#range(stop)
    print(i)


for i in range(2, 10):#range(start , stop)
    print(i)


for i in range(2, 10, 2):#range(start , stop, step)
    print(i)


#for i in range(2, 100, 2):



for i in range(1,4):
    for j in range(1,3):
        print(i,j)


for i in range(1,6):
    for j in range(i):
        print("*",end= " ")
    print()

for i in range(1,6):
    if i == 3:
        break
    print(i)

for i in range(1,6):
    if i == 3:
        continue
    print(i)

for i in range(1,6):
    print(i*2)

for i in range(1,6):
    print(i*i)

num = "shivam kashyap"
for i in num:
    print(i)

sq = {}

for i in range(1,4):
    sq[i] = i**2
print(sq)