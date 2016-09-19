# ЗАДАЧІ:
# 1. Взяти найбільші значення origin і new
# 2. Знайти по найбільшим значенням original і new найбільші букви
# 3. Порахувати відстань між цими буквами
# 4. Взяти декілька наступних по величині значень. Переконатись, що відстань однакова.
# 5. Вивести 2 результати: зміщення на відстань в кожну зі сторін
# x. Дати зручні і зрозумілі назви всім змінним
# x+1. Написати шифрацію з ключем і з генерацією рандомного
# x+2. Додати ключі до командної стрічки.

alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ь', ' ')

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
    ' ': 0.17
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
    ' ': 0
}

# Зчитуємо текст
#text = input('Введіть текст: ')
text = open('text.txt', encoding='utf8').read()
#print(text)

# Рахуємо к-сть літер разом і кожної окремо
letters = new.keys()
for element in letters:
    #print(element)
    i = 0
    for characters in text:
        if text[i] == element:
            new[element] += 1
        i += 1


print('=========================================')
print('Всіх літер: ' + str(len(text)))

print('Літер "е": ' + str(new['е']))

# frequency calculation algorithm
coefficient = new['е'] / len(text)
print('Відсотків "e": ' + str(coefficient))

# Розраховуємо і додаємо частоти для кожної літери в словник new
a = 0
for elements in new:
    b = alphabet[a]
    print('old ' + b + ' :' + str(new[b]))
    new[b] = new[b] / len(text)
    print('new ' + b + ' :' + str(new[b]))
    a += 1


# Масив з частотами оригінальних літер. Сортуєм ці частоти від найбільшої до найменшої.
print("FO")
frequency_original = []
a = 0
for elements_a in original:
    b = alphabet[a]
    a += 1
    frequency_original.append(original[b])

print(frequency_original)
frequency_original.sort(reverse=True)
print(frequency_original)
print(len(frequency_original))


# Масив з частотами літер вхідного тексту. Сортуєм ці частоти від найбільшої до найменшої.
print("FN")
frequency_new = []
a = 0
for elements_b in new:
    b = alphabet[a]
    a += 1
    frequency_new.append(new[b])

print(frequency_new)
frequency_new.sort(reverse=True)
print(frequency_new)
print(len(frequency_new))
