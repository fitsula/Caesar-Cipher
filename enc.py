alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ь')

text = open('text.txt', encoding='utf8').read()
print(text)

key = input('Введіть ключ: ')
print('Key = ' + key)

length = len(alphabet)
print('Довжина абетки: ' + str(length))


def caesar():
    new_text = ""
    for character in text:
        n = 0  # який номер елементу в alphabet
        done = 0
        for element in alphabet:
            if element == character:
                letter = (int(n) + int(key)) % int(length)
                new_text += alphabet[letter]
                done = 1
            n += 1

        if done == 0:
            new_text += character
    return new_text

print(caesar())
