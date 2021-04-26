def run():
    # square_nums = []

    # for i in range(1,101):
    #     if i % 3 != 0:
    #         print(i, number**2)
    #         square_nums.append(i**2)

    # # Imprime la lista resultado
    # for i in square_nums:
    #     print(i) 

    square_nums = [i**2 for i in range(1,101) if i % 3 != 0]

    # Imprime la lista resultado
    for i in square_nums:
        print(i) 


if __name__ == '__main__':
    run()