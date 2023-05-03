# Shopping list Organizor

shopping_list=[]
# Adding Items
user=int(input('Enter the Numbers of Items:'))
i=0
while i<user:
    item=input(f'Enter the Item {i+1} : ')
    shopping_list.append(item)
    i=i+1 

# Printing Item List
print('Your Item List for Shopping is:')
for y,itm in enumerate(shopping_list):
   print(f'Item {y+1} : {itm.title()}\n')

# Completed Item 
completed_list=[]
Range=int(input('Enter the Number of complted items: '))
for i in range(Range):
    ask_user = int(input(f"Enter Number {i+1}: \n"))
    completed_item = shopping_list[ask_user-1] 
    completed_list.append(completed_item)

# Printing Completed Item List
for y in completed_list:
    print('Completed Item List for Shopping is:')
    print([y],end=' ')

# Removing Items
'''removing_items=[]
num_range=int(input('Enter the Number of Removing items: '))
for z in range(num_range):
    User = int(input(f"Enter  Item to Remove {z+1}: \n")) 
    removing_items.append(User-1)
removing_items.sort(reverse=True)
for j in removing_items:
   print(f'\n {[removing_items.pop(j-1)]}\n')

# Printing Incomplete Item List
for y,itm in enumerate(shopping_list):
   print(f'Item {y+1} : {itm.title()}')

# Printing Final List'''

