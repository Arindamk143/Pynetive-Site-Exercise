l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_elements= l1[1::2]
print("The Odd element element index are: ")
print(odd_elements)

Even_Elements = l2[0::2]
print("The Even Indexes Are: ")
print(Even_Elements)

print("printing the third list: ")
a = list()
a.extend(Even_Elements)
a.extend(odd_elements)
print(a)