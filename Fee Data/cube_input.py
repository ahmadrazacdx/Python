from dict_class import fee

def cube(fee:dict):
    values=list(fee.values())
    user = input('Choose an option in Fee Details: ')
    if user.isdigit() and 1 <= int(user) <= len(values):
        index = int(user) - 1
        print('Value is :', values[index])
        cube=values[index]**3
        print(f'Cube of value is : {cube:.2f}')
    else:
        print('Invalid Option')
