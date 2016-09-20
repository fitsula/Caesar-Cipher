alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ю', 'я', 'ь')

text = open('enc.txt', encoding='utf8').read()
print(text)

key = input('Введіть ключ: ')
print('Key = ' + key)

length = len(alphabet)
print('Довжина абетки: ' + str(length))

i = 0
print('character in text: ')

original = []
new = []

for character in text:
    #print(text[i])

    #print(str(i) + " element in alphabet")
    n = 0
    for element in alphabet:
        if element == text[i]:
            alphabet_number = n % length
            #print('yes, element = ' + element + ' and text[i] = ' + text[i] + ' and = ' + str(n) + ' in alphabet - ' +\
                  #alphabet[alphabet_number])
            original.append(alphabet_number)
        #print(element)
        n += 1
    i += 1

for original_number in original:
    #print('Original number: ')
    #print(original_number)
    #print('New number: ')
    new_number = (int(original_number) - int(key)) % int(length)    # if dec - int(key), if enc + int(key)
    new.append(new_number)

print('Original: ', end='')
print(original)
print('New: ', end='')
print(new)

print('\n\n\n=====================')
print('Original text: ')
print(text, end='\n\n')
print('Encrypted text: ')


for characters in new:
    print(alphabet[characters], end='')


# string += character       # method for good future
