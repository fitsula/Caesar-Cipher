import random

parameters = {
    'action': 'enc',        # enc or dec
    'file': 'text.txt',     # 'print' for hand input
    'result': 'ps',          # p - print, s filename - save into filename, ps - print and save
    'key': 'gen',           # int number, gen - generate random key
    'accuracy': 3           # скільки найбільших букв порівнювати
}

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я')

alphabet_capital = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                    'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я')


if parameters['file'] == 'print':
    text = input('Type the text: ')
else:
    text = open(parameters['file'], encoding='utf8').read()


length = len(alphabet)


if parameters['key'] == 'gen':
    key = random.randint(1, length)
else:
    key = parameters['key']


if parameters['action'] == 'enc':

    def encryption():
        new_text = ""
        for character in text:
            n = 0  # який номер елементу в alphabet
            c = 0  # який номер елементу в alphabet_capital
            done = 0
            for element in alphabet:
                if element == character:
                    letter = (int(n) + int(key)) % int(length)
                    new_text += alphabet[letter]
                    done = 1
                n += 1

            if done != 1:
                for element in alphabet_capital:
                    if element == character:
                        letter = (int(c) + int(key)) % int(length)
                        new_text += alphabet_capital[letter]
                        done = 1
                    c += 1

            if done == 0:
                new_text += character
        return new_text

    if parameters['result'] == 'p':
        print(encryption())
    elif parameters['result'] == 's':
        result_file = open('new_text.txt', 'w', encoding='utf8')
        result_file.write(encryption())
    elif parameters['result'] == 'ps':
        print(encryption())
        result_file = open('new_text.txt', 'w', encoding='utf8')
        result_file.write(encryption())

elif parameters['action'] == 'dec':

    print('decode')

else:
    print('Restart application and choose "enc" for encoding or "dec" for decoding')
