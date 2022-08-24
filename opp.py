from typing.io import IO


class Parser:
    """
    Base class for parsing
    """
    def __init__(self, input='test_ling', lang_1='English', lang_2='Russian'):
        self.input = input
        self.lang_1 = lang_1
        self.lang_2 = lang_2

    def make_list(self, var: str, language: int) -> list:
        '''
        Makes a sheet of one language
        '''
        return var.split('\t')[language].split(';')

    def write_info(self, file: IO, word: str):
        '''
        Writes information to a file
        '''
        file.write(word.strip() + '\n')

    def parsing(self):
        '''
        Main function
        '''
        with open(f'{self.input}.txt', 'r', encoding='utf-8') as input, \
                open(f'{self.lang_1}.txt', 'a', encoding='utf-8') as language_1, \
                open(f'{self.lang_2}.txt', 'a', encoding='utf-8') as language_2:
            data = input.readlines()
            for string in data:
                english_words = self.make_list(string, 0)
                russian_words = self.make_list(string, 1)
                for eng_word in english_words:
                    for rus_word in russian_words:
                        self.write_info(language_1, eng_word)
                        self.write_info(language_2, rus_word)


isinstance = Parser()
isinstance.parsing()