# todos = open('todos.txt', 'a')

# print('put out the trash', file=todos)
# print('feed the cat', file=todos)
# print('Prepare tax return', file=todos)

# todos.close()


# tasks = open('todos.txt')

# for chore in tasks :
#     print(chore, end='')

# tasks.close()


with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')

