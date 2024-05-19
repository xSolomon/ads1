''' Tests for solution4_5 function. '''

import unittest
from random import choice
from solution4_5 import is_parentheses_sequence_balanced as balance

class IsParenthesesSequenceBalancedTests(unittest.TestCase):
    ''' Tests is_parentheses_sequence_balanced() function '''
    def generate_large_balanced_sequence(self) -> str:
        ''' Generates large balanced sequence of "(" and ")". '''
        sequence_length : int = 1000
        balance_indicator : int = 0
        sequence : str = ''
        parentheses : list[tuple[str, int]] = [('(', 1), (')', -1)]
        for i in range(sequence_length):
            if balance_indicator == 0:
                sequence += '('
                balance_indicator += 1
                continue
            if sequence_length - i - balance_indicator == 0:
                sequence += ')'
                balance_indicator -= 1
                continue
            what_to_generate : tuple[str, int] = choice(parentheses)
            sequence += what_to_generate[0]
            balance_indicator += what_to_generate[1]
        return sequence

    def generate_large_unbalanced_sequence(self) -> str:
        ''' Generates large unbalanced sequence of "(" and ")". '''
        sequence_length : int = 1000
        balance_indicator : int = 0
        sequence : str = ''
        parentheses : list[tuple[str, int]] = [('(', 1), (')', -1)]
        for _ in range(sequence_length - 1):
            what_to_generate : tuple[str, int] = choice(parentheses)
            sequence += what_to_generate[0]
            balance_indicator += what_to_generate[1]
        sequence += choice(parentheses)[0] if balance_indicator != 1 else '('
        return sequence

    def test_on_empty_string(self) -> None:
        ''' Tests on empty string. Expected True. '''
        self.assertTrue(balance(''))

    def test_on_string_without_parentheses(self) -> None:
        ''' Tests case when string contains no parentheses. Expected True. '''
        self.assertTrue(balance('abcdef123456.,/'))

    def test_on_string_with_single_parenthesis(self) -> None:
        ''' Tests on "(" and ")". Expected False. '''
        self.assertFalse(balance('('))
        self.assertFalse(balance(')'))

    def test_on_unbalanced_sequences(self) -> None:
        ''' Tests on some predefined cases of unbalanced sequences.
            Expected False for each sequence. '''
        sequences : list[str] = ['((((', ')))', ')(', '((())))', '(((()))', '()())', '()(()))(']
        for sequence in sequences:
            with self.subTest(string = sequence):
                self.assertFalse(balance(sequence))

    def test_on_balanced_sequences(self) -> None:
        ''' Tests on some predefined cases of balanced sequences.
            Expected True for each sequence. '''
        sequences : list[str] = ['()', '((()))', '()(())((()))((()))()', '((()((()()))))']
        for sequence in sequences:
            with self.subTest(string = sequence):
                self.assertTrue(balance(sequence))

    def test_on_large_random_balanced_sequences(self) -> None:
        ''' Tests on large random balanced sequences.
            Expected True for each sequence. '''
        test_times : int = 1000
        for _ in range(test_times):
            sequence : str = self.generate_large_balanced_sequence()
            with self.subTest(string = sequence):
                self.assertTrue(balance(sequence))

    def test_on_large_random_unbalanced_sequences(self) -> None:
        ''' Tests on large random unbalanced sequences.
            Expected False for each sequence. '''
        test_times : int = 1000
        for _ in range(test_times):
            sequence : str = self.generate_large_unbalanced_sequence()
            with self.subTest(string = sequence):
                self.assertFalse(balance(sequence))

unittest.main()
