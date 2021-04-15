#Exercise 1
aLsit = [100, 200, 300, 400, 500]
# Expected outout [500, 400, 300, 200, 100]
print(aLsit[::-1])

# Exercise 2: Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
# Expected output: ['My', 'name', 'is', 'Kelly']

list3 = [i + j for i, j in zip(list1, list2)]
print(list3)


# Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
#Expected output: [1, 4, 9, 16, 25, 36, 49]
b = []
for i in aList: 
  b.append(i * i)
print(b)

#Alternative Solution
#aList =  [x * x for x in aList]
#print(aList)


# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3 = []
for i in list1:
    for j in list2:
        list3.append(i+ " " + j)
print(list3)

#Alternative Solution
#resList = [x+y for x in list1 for y in list2]
#print(resList)


# Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1
# should display item in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100
for x, y in zip(list1, list2[::-1]):
    print(x, y)