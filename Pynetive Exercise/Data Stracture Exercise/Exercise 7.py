first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("first set is superset of second set: ", first_set.issubset(second_set))
print("first set is superset of second set: ", second_set.issubset(first_set))

print("first set is superset of second set: ", first_set.issuperset(second_set))
print("first set is superset of second set: ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
