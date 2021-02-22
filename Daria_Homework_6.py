##################################################
my_list = ['qwe', 'rty', 'uio', 'opd', 'ljh']
new_list = [0]
for index, symbol in enumerate(my_list):
    if not index % 2:
        new_list.append(symbol)
    elif index % 2:
        new_list.append(symbol[::-1])
print(new_list)
