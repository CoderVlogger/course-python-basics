
print('1 - add element')
print('2 - change element')
print('3 - delete element')
print('0 - exit')

storage = []

while True:
    print('\n\n')
    operation = input('Please enter operation: ')
    if operation == 0:
        break

    if operation == 1:
        item = input('Please enter item: ')
        storage.append(item)

    if operation == 2:
        index = input('Please enter item\'s index: ')
        new_item = input('Please enter new item: ')
        storage[index] = new_item

    if operation == 3:
        index = input('Please enter item\'s index: ')
        del storage[index]

    print(storage)
