
guest_list = ['hellen','carlos']

print(f'Hey {guest_list[0].title()}!, I would like to invite you to a dinner .')
print(f'Hey {guest_list[1].title()}!, I would like to invite you to a dinner this weekend.')

print(len(guest_list))

print(f'Oh!, {guest_list[1].title()} can not make it')

guest_list[1] = 'jacquie'

print(f'Hey {guest_list[0].title()} and {guest_list[1].title()}, I  would like to invite you to a dinner.')

print('Oh!, I found a bigger table for tongiht!!!')

guest_list.insert(0,'alicia')
guest_list.append('bettina')

print(f'Hey {guest_list}, come over tonight!')

print('Sorry, only two people!')

rejected_one = guest_list.pop(0)
print(f"I'm sorry {rejected_one.title()} you are not coming.")

rejected_two = guest_list.pop(1)
print(f"I'm sorry {rejected_two.title()}, you are not coming.")

print (f'{guest_list[0].title()},{guest_list[1].title()} are still invited!')

del guest_list[0]

print(guest_list)

del guest_list[0
]

print(guest_list)



