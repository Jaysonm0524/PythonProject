def taking_order():
    more = 'yes'
    while more == "yes" or more == 'Yes':
        print('What will it be?')
        order = input()
        order_list.append(order)

        print('Anything else? [yes/no]')
        more = input()


def approach():
    response = input()

    if response == 'No' or response == 'no':
        print('Are you ready to order now?')
        approach()
    else:
        taking_order()


order_list = []
print('Hello, I am your Butler Today.')
print('Are you ready to order?')

approach()

print("So that'll be ", order_list)
print("Is that correct?")

correct = input()

if correct == 'yes' or correct == 'Yes':
    print('And a name for that order?')
    name = input()
    print('Okay, ', name, ' Your order should be out soon.')
else:
    print('Can I take your order again then?')
    approach()