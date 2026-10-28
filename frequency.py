s = "shivam"

max_char = "" 
max_count = 0

for i in s :
    count = 0
    for j in s :
        if j == i:
            count += 1
    if count>max_count:
        max_count = count
        max_char = i 
       


s ="education"
v ="aeiouAEIOU"
freq ={}
for i in v:
    freq[i]= 0
    for j in s:
        if i==j:
            freq[i]+=1
print(freq)
    