class Parser:
    """
    Base class for parsing
    """

    def make_list(self, var: str, language: int):
        '''
        Makes a sheet of one language
        '''
        return var.split('\t')[language].split(';')

    def write_info(self, file, word: str):
        '''
        Writes information to a file
        '''
        file.write(word.strip() + '\n')

    def parsing(self):
        '''
        Main function
        '''
        with open('test_ling.txt', 'r', encoding='utf-8') as input, \
                open('English.txt', 'a', encoding='utf-8') as english, \
                open('Russian.txt', 'a', encoding='utf-8') as russian:
            data = input.readlines()
            for string in data:
                english_words = self.make_list(string, 0)
                russian_words = self.make_list(string, 1)
                for eng_word in english_words:
                    for rus_word in russian_words:
                        self.write_info(english, eng_word)
                        self.write_info(russian, rus_word)


isinstance = Parser()
isinstance.parsing()