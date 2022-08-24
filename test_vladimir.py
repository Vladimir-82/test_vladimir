with open('test_ling.txt', 'r', encoding='utf-8') as input, \
        open('English.txt', 'a', encoding='utf-8') as english, \
        open('Russian.txt', 'a', encoding='utf-8') as russian:
    data = input.readlines()
    for string in data:
        eng, rus = string.split('\t')[0].split(';'), string.split('\t')[1].split(';')
        for eng_word in eng:
            for rus_word in rus:
                english.write(eng_word.strip() + '\n')
                russian.write(rus_word.strip() + '\n')