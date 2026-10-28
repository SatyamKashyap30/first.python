null_dict = {}
null_dict["name"] = "shivam kashyap"
print(null_dict)

student ={
    "name":"shivam kashyap",
    "subjects":{
        "phy":98,
        "chem":97,#nested dictionary
        "math":99
    }
}
new_dict = {"city":"patna","age":20}
student.update({"city": "darbhanga"})
student.update(new_dict)
pairs = list(student.items())
print(student["subjects"]["math"]) 
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(student.items())#tuple
print(pairs[0])
print(pairs[1])
print(student["name"])
print(student.get("name"))
print(student)
print(student)



dict = {
    "name" : "shivam kashyap",#string
    "subjects" : ["python","C","Java"],#list
    "topics" : ("dict","set"),#tuple
    "age": 19,
    "is_adult" : True,
    "marks" : 94.5,
    12.99 : 678
    }

print(dict)
print(type(dict))
print(dict["name"])
print(dict["topics"])
print(dict[12.99])
print(dict["age"])