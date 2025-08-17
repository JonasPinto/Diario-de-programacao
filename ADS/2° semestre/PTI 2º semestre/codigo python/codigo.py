def query_bin(array, index_init, index_final, item):
    if index_init > index_final:
        return 'animal não cadastrado'
    index = (index_init + index_final) // 2
    if array[index] == item:
        return item
    elif array[index] > item:
        return query_bin(array, index_init,index - 1, item)
    else:
        return query_bin(array, index + 1, index_final, item)

print('_' * 30)
print('\nConsulta de animais')
print('_' * 30)
item = int(input('Digite o codigo do animal:'))
values = [0, 10, 20, 30, 40, 50, 60, 100]
print("result: ",query_bin(values, 0, len(values), item))

