from typing.io import IO


class Parser:
    """
    Base class for parsing
    """
    LANG_SEP = '\t'
    WORD_SEP = ';'
    def __init__(self, input_file='test_ling', lang_1='English', lang_2='Russian'):
        self.input_file = input_file
        self.lang_1 = lang_1
        self.lang_2 = lang_2

    def make_list(self, value: str, is_lang_from: bool = True) -> list:
        '''
        Makes a sheet of one language
        '''
        part = 0 if not is_lang_from else 1
        words = value.split(Parser.LANG_SEP)[part].split(Parser.WORD_SEP)
        return words

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
                            lang_from_words = self.make_list(string, first_language)
                            lang_to_words = self.make_list(string, second_language)
                            for from_word in lang_from_words:
                                for to_word in lang_to_words:
                                    self.write_info(language_1, from_word)
                                    self.write_info(language_2, to_word)


instance = Parser()
instance.parsing()