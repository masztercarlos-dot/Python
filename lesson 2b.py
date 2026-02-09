# python dictionary 
person= {
         "firstname" :"John",
         "lastname":"Doe",
         "age":25,
         "colors":["red" ,"blue"],
         "salary" :5000 ,
}
# show outputs 
print(person)

# print age
print(person["age"])

# print salary
print(person["salary"])

# update date to 34
person["age"] =34
# show ouput
print(person)

# delete lastname
del person ["lastname"]

# shoe outputs
print(person)