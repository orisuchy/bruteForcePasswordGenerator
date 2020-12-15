def pass_gen(chars, length):
    for current in range(length):
        pass_list = [i for i in chars]
        for x in range(current):
            pass_list = [y + i for i in chars for y in pass_list]
    return pass_list


charList = str(input('Input char list:\n'))
passLength = int(input('\nInput password length:\n'))
generatedList = pass_gen(charList, passLength)
print(f'\nTotal - {len(generatedList)} options')
print(f'\nGenerated options:\n{generatedList}')