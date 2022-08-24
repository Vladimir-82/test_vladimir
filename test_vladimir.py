with open('test_ling.txt', 'r', encoding='utf-8') as input, \
        open('English.txt', 'a', encoding='utf-8') as english, \
        open('Russian.txt', 'a', encoding='utf-8') as russian:
    data = input.readlines()
    for string in data:
        english_words, russian_words = string.split('\t')[0].split(';'), string.split('\t')[1].split(';')
        for eng_word in english_words:
            for rus_word in russian_words:
                english.write(eng_word.strip() + '\n')
                russian.write(rus_word.strip() + '\n')