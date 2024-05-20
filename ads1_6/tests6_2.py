''' Tests for lesson 6 task 2 solution. '''

import unittest
from solution6_2 import is_palindrom

class IsPalindromTests(unittest.TestCase):
    ''' Tests is_palindrom function. '''
    def test_on_empty_string(self) -> None:
        ''' Tests on empty string. Expected True. '''
        self.assertTrue(is_palindrom(''))

    def test_on_single_char_string(self) -> None:
        ''' Tests on string with only one char. Expected True. '''
        self.assertTrue(is_palindrom('a'))

    def test_on_predefined_palindroms(self) -> None:
        ''' Tests on some palindrom strings. Expected True for each string. '''
        palindrom_list : list[str] = ['radar', 'saippuakivikauppias',
            '1234567890a0987654321', 'qwerty.,!!!,.ytrewq', '&&)))zz1123c$#^#$c3211zz)))&&']
        for palindrom in palindrom_list:
            with self.subTest(string = palindrom):
                self.assertTrue(is_palindrom(palindrom))

    def test_on_predefined_not_palindroms(self) -> None:
        ''' Tests on some not palindrom strings. Expected False for each string. '''
        not_palindrom_list : list[str] = ['1234567890', 'qwerty', '!@#$^&*', '123zx321',
            '12', '<<</|>>>', '-===-=======-']
        for not_palindrom in not_palindrom_list:
            with self.subTest(string = not_palindrom):
                self.assertFalse(is_palindrom(not_palindrom))

unittest.main()
