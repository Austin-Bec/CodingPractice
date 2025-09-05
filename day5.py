fruits = ["apple", "banana", "cherry"]
print   (fruits)
print(fruits[0])
print(fruits[1])

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

del fruits[0]
print(fruits)

for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("Apple is in the list.")