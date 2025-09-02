x=100
get_number = float(input('Enter a number: '))
while get_number<x:
    print('The number is less than the number.')
    get_number = float(input('Enter a number: '))
while get_number>x:
    print('The number is greater than the number.')
    get_number = float(input('Enter a number: '))
    while get_number<x:
        print('The number is less than the number.')
        get_number = float(input('Enter a number: '))
while get_number==x:
    print('The number is equal to the number.')
    break