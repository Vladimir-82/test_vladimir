from typing.io import TextIO


class Parser:
    """
    Parsing the source file, finding pairs of words
    and saving them to different files
    """
    LANG_SEP = '\t'
    WORD_SEP = ';'

    def __init__(self,
                 input_file_name: str = 'test_ling',
                 lang_from_file_name: str = 'English',
                 lang_to_file_name: str = 'Russian'):
        self.input_file_name = input_file_name
        self.lang_from_file_name = lang_from_file_name
        self.lang_to_file_name = lang_to_file_name

    def parsing(self):
        '''
        Splitting one dictionary file into two
        with words from the same language
        '''
        try:
            with open(f'{self.input_file_name}.txt', 'r',
                      encoding='utf-8') as input_file:
                input_data = input_file.readlines()
        except IOError:
            print('Error: Unsupported file!')
        except NameError:
            print('Error: File does not exist!')
        else:
            with open(f'{self.lang_from_file_name}.txt', 'a',
                      encoding='utf-8') as lang_from_file, \
                    open(f'{self.lang_to_file_name}.txt', 'a',
                         encoding='utf-8') as lang_to_file:
                for words_string in input_data:
                    words_from = self._get_words(words_string)
                    words_to = self._get_words(words_string, is_from=False)
                    for word_from in words_from:
                        for word_to in words_to:
                            self._write_word(lang_from_file, word_from)
                            self._write_word(lang_to_file, word_to)

    def _get_words(self, value: str, is_from: bool = True) -> list:
        """
        Get the one language words list.
        Is_from flag points to the words of first language
        """
        part = 0 if is_from else 1
        words = value.split(self.LANG_SEP)[part].split(self.WORD_SEP)
        return words

    @staticmethod
    def _write_word(file: TextIO, word: str):
        '''
        Writes word to a file
        '''
        file.write(word.strip() + '\n')


instance = Parser()
instance.parsing()
