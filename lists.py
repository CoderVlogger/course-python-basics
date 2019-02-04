# Python Data Collections
# List
# Tuple
# Set
# Dictionary

my_list1 = [1, 2, 3, 4]
my_list2 = ['nissan', 'mercedes', 'bmw']
my_list3 = [1, 'apple', 2, 'microsoft', 3, 'google']

print(my_list1[0])
print(len(my_list1))

for i in my_list2:
    print(i)


my_list3.append(4)
my_list3.append('facebook')

for i in my_list3:
    print(i)

my_list3.extend([5, 'amazon'])

for i in my_list3:
    print(i)

my_list3[len(my_list3)-1] = 'uber'

for i in my_list3:
    print(i)

del my_list3[len(my_list3)-1]

for i in my_list3:
    print(i)
