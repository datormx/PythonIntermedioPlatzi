from functools import reduce

def run():
    # Filtrar números impares
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x : x%2 != 0, my_list))

    print(odd)

    # Mapear números al cuadrado
    my_list = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, my_list))

    print(squares)

    # Reducir los elementos a un único valor (múltiplicando uno tras otro para este ejemmplo)
    my_list = [2, 2, 3, 2, 5]

    all_multiplied = reduce(lambda a,b: a * b, my_list)

    print(all_multiplied)



if __name__ == '__main__':
    run()