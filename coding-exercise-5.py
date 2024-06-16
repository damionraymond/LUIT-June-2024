num_days = int(input('How many days ago have you purchased the item? '))
used_item = input('Have you used the item at all [y/n]? ')
item_broke = input('Has the item broken down on its own [y/n]? ')

if num_days <= 10 and used_item == 'n' or item_broke == 'y': 
    print('You can get a refund.')
else:
    print('You cannot get a refund.')