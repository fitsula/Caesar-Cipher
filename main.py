# ЗАДАЧІ:
# 1. Змусити код працювати
# 2. Переписати enc.py з двома параметрами - enc і dec
# 3. Написати шифрацію з ключем і з генерацією рандомного


parameters = {
    'action': 'dec',        # enc or dec
    'file': 'enc.txt',
    'result': 'p',          # p - print, s filename - save into filename, ps - print and save
    'key': '5',             # int number, gen - generate random key
    'accuracy': 3           # скільки найбільших букв порівнювати
}

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ь')

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
    'ю': 0.006205614176579968,
    'я': 0.01711584559894258,
    'ь': 0.01043976969778435,
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
            key = (int(numbersNew[i]) - int(numbersOriginal[i])) % int(len(alphabet))

            print('=================')
            print('numbersOriginal[i] = ' + str(numbersOriginal[i]))
            print('len(alphabet) = ' + str(len(alphabet)))
            print('str(numbersNew[i]) = ' + str(numbersNew[i]))
            print('len(alphabet) = ' + str(len(alphabet)))


            keys.append(key)
            #print('Key ' + str(i) + ' = ' + str(key))
            i += 1

        return keys
    keys = keySearch()
    return keys

    keySearch()

frequencyKey(parameters['accuracy'])

def finalKey():
    k = 0
    keys = frequencyKey(parameters['accuracy'])

    result = 'good'
    for keyCurrent in keys:
        print(keyCurrent)
        if k > 0:
            if keys[k] == keys[k - 1]:
                final = keys[k]
            else:
                print('bad')
                result = 'bad'
        k += 1

    if result == 'bad':
        final = 'bad'

    return final  # add to global

print('Final Key: ')
print(finalKey())
