# python list -it is an ordered collection of items
items=["Honda" ,"Mazda","Surf", "Volkswagon" ," Subaru"]
# show outputs
print(items)

# print item at index 2
print(items[2])

# print item at index 3
print(items[3])

# apending new items 
# append BMW
items.append("BMW")

# show output

print(items)

# inserting items at specific index 
# insert toyota at index 2
items.insert(2,"Toyota")
# show output

print(items)

# slacing 
# 1. slice from index 2 to 5
print(items[ 2:5])

# 2. print frominde 4 and below 

print(items[: 4])

# 3. print from inde 3 and above

print(items [3:])