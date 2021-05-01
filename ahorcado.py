from random import randint
import os


def read_word():
    words = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line)

    word_quantity = len(words)
    word_position = randint(0, word_quantity)
    selected_word = words[word_position]
    selected_word = selected_word[:-1]

    return selected_word


def interface(word):
    characters = [char for char in word]    
    empty_characters = ['_' for char in characters]

    while characters != empty_characters:
        os.system('clear')
        separator =' '
        print('¡Adivina la palabra!\n')
        print(separator.join(empty_characters))
        new_char = input('\nIngresa una letra: ')
        assert new_char.isalpha(), "Solo debes agregar letras."
        empty_characters = hangman(characters, empty_characters, new_char)

    os.system('clear')
    separator = ''
    print(f'\n¡Felicidades, la palabra es {separator.join(empty_characters)}!')


def hangman(characters, empty_characters, input_char):
    for position, character in enumerate(characters):
        if character == input_char:
            empty_characters[position] = character
    
    return empty_characters


def run():
    word = read_word()
    interface(word)



if __name__ == '__main__':
    run()