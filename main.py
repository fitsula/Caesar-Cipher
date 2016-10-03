import random

parameters = {
    'action': 'dec',        # enc or dec
    'file': 'text.txt',     # 'print' for hand input
    'result': 'ps',         # p - print, s filename - save into filename, ps - print and save
    'key': 'gen',           # int number, gen - generate random key
    'accuracy': 3           # скільки найбільших букв порівнювати
}

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я')

alphabet_capital = ('А', 'Б', 'В', 'Г', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р',
                    'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я')


# the frequency of occurrence of letters
original = {
    'а': 0.06509174003629276,
    'б': 0.01276967538141004,
    'в': 0.04719179156305307,
    'г': 0.011436700495104958,
    'д': 0.025068889038241816,
    'е': 0.0374465129825033,
    'є': 0.0026659497726101663,
    'ж': 0.00719134350426776,
    'з': 0.017138248538208212,
    'и': 0.050933082420413556,
    'і': 0.04648609897618568,
    'ї': 0.00319241884535251,
    'й': 0.010484575576315613,
    'к': 0.02736519031296906,
    'л': 0.028518941685149093,
    'м': 0.021237986423818803,
    'н': 0.04566839169299012,
    'о': 0.06831776329054372,
    'п': 0.021181979075654726,
    'р': 0.040627730358223,
    'с': 0.02876537401707104,
    'т': 0.034310101485314874,
    'у': 0.026077021305195243,
    'ф': 0.0014673925218988732,
    'х': 0.00780742433407263,
    'ц': 0.00386450702332146,
    'ч': 0.012489638640589645,
    'ш': 0.00692250823308018,
    'щ': 0.004514192262024778,
    'ь': 0.01043976969778435,
    'ю': 0.006205614176579968,
    'я': 0.01711584559894258,
}

new = {
    'а': 0,
    'б': 0,
    'в': 0,
    'г': 0,
    'д': 0,
    'е': 0,
    'є': 0,
    'ж': 0,
    'з': 0,
    'и': 0,
    'і': 0,
    'ї': 0,
    'й': 0,
    'к': 0,
    'л': 0,
    'м': 0,
    'н': 0,
    'о': 0,
    'п': 0,
    'р': 0,
    'с': 0,
    'т': 0,
    'у': 0,
    'ф': 0,
    'х': 0,
    'ц': 0,
    'ч': 0,
    'ш': 0,
    'щ': 0,
    'ь': 0,
    'ю': 0,
    'я': 0,
}


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

    if parameters['key'] == 'gen':
        def key_search():

            # Рахуємо к-сть літер
            def letters_calculation():
                for element in alphabet:
                    for character in text:
                        if character == element:
                            new[element] += 1
                for element in alphabet_capital:
                    for character in text:
                        if character == element:
                            new[element.lower()] += 1

            letters_calculation()

            # Розраховуємо і додаємо частоти для кожної літери в словник new
            def frequency_calculation():
                for element in new:
                    new[element] /= len(text)  # frequency calculation algorithm

            frequency_calculation()

            # Масив з частотами оригінальних літер. Сортуєм ці частоти від найбільшої до найменшої.
            def frequency_original_sort():
                frequency = []
                for element in original:
                    frequency.append(original[element])
                frequency.sort(reverse=True)
                return frequency

            frequency_original_sort()

            # Масив з частотами літер вхідного тексту. Сортуєм ці частоти від найбільшої до найменшої.
            def frequency_new_sort():
                frequency = []
                for element in new:
                    frequency.append(new[element])
                frequency.sort(reverse=True)
                return frequency

            frequency_original_sort()
            frequency_new_sort()

            # Вибираємо потрібну к-сть найбільших значень
            def popular_numbers(accuracy):
                frequency_original = frequency_original_sort()
                frequency_original = frequency_original[0:accuracy]
                frequency_new = frequency_new_sort()
                frequency_new = frequency_new[0:accuracy]

                def numbers_array(array, freq_array):
                    numbers = []
                    for frequency in freq_array:
                        i = 0
                        for element in alphabet:
                            if array[element] == frequency:
                                numbers.append(i)
                            i += 1

                    return numbers

                print('Popular Original Numbers = ' + str(numbers_array(original, frequency_original)))
                print('Popular New Numbers = ' + str(numbers_array(new, frequency_new)))

                # Обчислюємо i створюємо масив з ключами
                def key_search_array():
                    numbers_original = numbers_array(original, frequency_original)
                    numbers_new = numbers_array(new, frequency_new)
                    i = 0
                    keys = []
                    for element in numbers_array(new, frequency_new):
                        key = (int(numbers_new[i]) - int(numbers_original[i])) % int(len(alphabet))
                        keys.append(key)
                        i += 1

                    return keys

                keys = key_search_array()
                return keys

            def final_key():
                k = 0
                keys = popular_numbers(parameters['accuracy'])

                result = 'good'
                final = 'bad'
                for current_key in keys:
                    if k > 0:
                        if keys[k] == keys[k - 1]:
                            final = keys[k]
                        else:
                            result = 'bad'
                    k += 1

                if result == 'bad':
                    final = 'bad'

                return final

            key = final_key()
            return key

        print(key_search())
    else:
        def decode():
            print('you have key, but now you must decode your text using this key')

else:
    print('Restart application and choose "enc" for encoding or "dec" for decoding')
