from random import sample


sample_list = [34, 54, 67, 89, 11, 43, 94]
print("printing the simple element: ",sample_list)
a = sample_list.pop(4)
print(" after removeing the 4th element: ", sample_list)

sample_list.insert(2,a)
print("iafter inserting 2nd element on index: ", sample_list)

sample_list.append(a)
print("after adding the last element from index a: ", sample_list)
