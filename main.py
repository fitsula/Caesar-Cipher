# ЗАДАЧІ:
# 1. Взяти декілька наступних по величині значень. Переконатись, що відстань однакова.
# 2. Вивести 2 результати: зміщення на відстань в кожну зі сторін
# x. Написати шифрацію з ключем і з генерацією рандомного


parameters = {
    'action': 'dec',        # enc or dec
    'file': 'Diahnostyka_i_likuvannia_nevidkladnyh_staniv.txt',
    'result': 'p',          # p - print, s filename - save into filename, ps - print and save
    'key': '5',             # int number, gen - generate random key
    'accuracy': 10           # скільки найбільших букв порівнювати
}

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ь')

# the frequency of occurrence of letters
original = {
    'а': 0.072,
    'б': 0.017,
    'в': 0.052,
    'г': 0.016,
    'д': 0.035,
    'е': 0.017,
    'є': 0.008,
    'ж': 0.009,
    'з': 0.023,
    'и': 0.061,
    'і': 0.057,
    'ї': 0.006,
    'й': 0.008,
    'к': 0.035,
    'л': 0.036,
    'м': 0.031,
    'н': 0.065,
    'о': 0.094,
    'п': 0.029,
    'р': 0.047,
    'с': 0.041,
    'т': 0.055,
    'у': 0.04,
    'ф': 0.001,
    'х': 0.012,
    'ц': 0.006,
    'ч': 0.018,
    'ш': 0.012,
    'щ': 0.001,
    'ю': 0.004,
    'я': 0.029,
    'ь': 0.029,
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
    'ю': 0,
    'я': 0,
    'ь': 0,
}

# Зчитуємо текст
if parameters['file'] == 'no':
    text = input('Введіть текст: ')
else:
    text = open(parameters['file'], encoding='utf8').read()
#print(text)  # DEBUG

print('len text = ' + str(len(text)))

# Рахуємо к-сть літер разом і кожної окремо
def lettersCalculation(text):
    letters = new.keys()
    for element in letters:
        #print(element)
        i = 0
        for characters in text:
            if text[i] == element:
                new[element] += 1
            i += 1

lettersCalculation(text)


#print('Всіх літер: ' + str(len(text)))         # DEBUG
#print('Літер "е": ' + str(new['е']))           # DEBUG

# frequency calculation algorithm
#coefficient = new['е'] / len(text)             # DEBUG
#print('Відсотків "e": ' + str(coefficient))    # DEBUG

# Розраховуємо і додаємо частоти для кожної літери в словник new
def frequencyCalculation():
    i = 0
    for element in new:
        a = alphabet[i]
        #print('old ' + a + ' :' + str(new[a]))  # DEBUG
        new[a] /= len(text)    # frequency calculation algorithm
        #print('new ' + a + ' :' + str(new[a]))    # DEBUG
        i += 1

frequencyCalculation()


# Масив з частотами оригінальних літер. Сортуєм ці частоти від найбільшої до найменшої.
def frequencyOriginalSort():
    #print("FO")    # DEBUG
    frequency = []
    a = 0
    for element in original:
        b = alphabet[a]
        a += 1
        frequency.append(original[b])

    #print(frequency_original)    # DEBUG
    frequency.sort(reverse=True)
    #print(frequency_original)    # DEBUG
    #print(len(frequency_original))    # DEBUG
    return frequency


# Масив з частотами літер вхідного тексту. Сортуєм ці частоти від найбільшої до найменшої.
def frequencyNewSort():
    #print("FN")    # DEBUG
    frequency = []
    a = 0
    for element in new:
        b = alphabet[a]
        a += 1
        frequency.append(new[b])

    #print(frequency_new)    # DEBUG
    frequency.sort(reverse=True)
    #print(frequency_new)    # DEBUG
    #print(len(frequency_new))    # DEBUG
    return frequency

frequencyOriginalSort()
frequencyNewSort()

# Вибираємо потрібну к-сть найбільших значень
def frequencyKey(accuracy):
    frequencyOriginal = frequencyOriginalSort()    # напевно не потрібно. ми ітак знаємо, які букви в нас найчастіше
    frequencyOriginal = frequencyOriginal[0:accuracy]                     # зустрічаються. але краще так, ніж вручну
    frequencyNew = frequencyNewSort()
    frequencyNew = frequencyNew[0:accuracy]

    print('Freq Original ' + str(frequencyOriginal))    # DEBUG
    print('Freq New ' + str(frequencyNew))    # DEBUG

    def popularNumbers(array, freqArray):
        numbers = []
        for frequency in freqArray:
            print(frequency)    # DEBUG
            i = 0
            for element in alphabet:
                if array[element] == frequency:
                    print(str(element) + ' = ' + str(array[element]) + ' = ' + str(frequency) + ' = ' + str(alphabet[i]) + ' = ' + str(i))    # DEBUG
                    numbers.append(i)
                i += 1

        return numbers

    print('Popular Numbers = ' + str(popularNumbers(original, frequencyOriginal)))
    print('Popular Numbers = ' + str(popularNumbers(new, frequencyNew)))

    def keySearch():
        numbersOriginal = popularNumbers(original, frequencyOriginal)
        numbersNew = popularNumbers(new, frequencyNew)
        i = 0
        keys = []
        for element in popularNumbers(new, frequencyNew):
            key = int(numbersOriginal[i]) % int(len(alphabet)) - int(numbersNew[i]) % int(len(alphabet))

            print('=================')
            print('numbersOriginal[i] = ' + str(numbersOriginal[i]))
            print('len(alphabet) = ' + str(len(alphabet)))
            print('str(numbersNew[i]) = ' + str(numbersNew[i]))
            print('len(alphabet) = ' + str(len(alphabet)))


            keys.append(key)
            print('Key ' + str(i) + ' = ' + str(key))

            if i > 0:
                if i == i - 1:
                    result = 'All fine'
                else:
                    result = 'All bad'


            i += 1
        print(result)
        print(keys)

    keySearch()

frequencyKey(parameters['accuracy'])
