def run():
    # numbers = {}

    # for i in range (1, 101):
    #     if i % 3 != 0:
    #         numbers.update({i : i**3}) # numbers[i] = i**3

    # print(numbers)

    my_dict = {i : i**3 for i in range(1, 101) if i % 3 != 0}

    print(my_dict)



if __name__ == '__main__':
    run()