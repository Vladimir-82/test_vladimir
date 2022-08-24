from typing.io import IO


class Parser:
    """
    Base class for parsing
    """
    lang_sep = '\t'
    word_sep = ';'
    def __init__(self, input_file='test_ling', lang_1='English', lang_2='Russian'):
        self.input_file = input_file
        self.lang_1 = lang_1
        self.lang_2 = lang_2

    def make_list(self, var: str, language: int) -> list:
        '''
        Makes a sheet of one language
        '''
        return var.split(Parser.lang_sep)[language].split(Parser.word_sep)

    def write_info(self, file: IO, word: str):
        '''
        Writes information to a file
        '''
        file.write(word.strip() + '\n')

    def parsing(self):
        '''
        Main function
        '''
        first_language = 0
        second_language = 1
        try:
            with open(f'{self.input_file}.txt', 'r', encoding='utf-8') as input:
                data = input.readlines()
        except IOError:
            print('Unsupported file!')
        else:
            with open(f'{self.lang_1}.txt', 'a', encoding='utf-8') as language_1, \
                    open(f'{self.lang_2}.txt', 'a', encoding='utf-8') as language_2:
                        for string in data:
                            english_words = self.make_list(string, first_language)
                            russian_words = self.make_list(string, second_language)
                            for eng_word in english_words:
                                for rus_word in russian_words:
                                    self.write_info(language_1, eng_word)
                                    self.write_info(language_2, rus_word)


isinstance = Parser()
isinstance.parsing()