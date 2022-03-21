list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

a = [x + y for x in list1 for y in list2]
print(a)