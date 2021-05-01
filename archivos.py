def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Facundo', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print('El archivo names.txt ha sido creado.')


def write_append():
    names = ['Jorge', 'Tuomas', 'Carmen', 'Juan', 'Silvia']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()
    # write()
    write_append()


if __name__ == '__main__':
    run()