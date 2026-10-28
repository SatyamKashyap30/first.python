collection = {1,2,3,4}
print(collection)
print(type(collection))
collection1 = {} #empty dictionary
print(type(collection1))
set1 = set() #empty dictionary;syntax
print(type(set1))

set = {1,2,3,4,4,4,"hello world","shivam"}
print(set)
print(type(set))
print(len(set))#total number of items

shivam = {1,2,3,4,5,5,"mango","rungta"}
shivam.add("car")
shivam.add("bihar")
shivam.add(456789)
shivam.add(1)
shivam.remove(5)
shivam.remove("mango")
shivam.clear() #jo add hoga wahi clear hoga bas
print(len(shivam))
print(shivam)


set1 = {1,2,3,4,}
set2 = {2,3,4}
print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{2,3,4}