''' Tests for function from lesson 4 task 6 solution. '''

import unittest
from solution4_1 import Stack
from solution4_6 import eval_expression_in_postfix_form as eval_postfix

class EvalExpressionInPostfixFormTests(unittest.TestCase):
    ''' Tests for eval_expression_in_postfix_form() function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.stack : Stack = Stack()

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        del self.stack

    def push_postfix_expression_to_stack(self, expression : str) -> None:
        ''' Save postfix expression in stack for testing its evaluation. '''
        token_list : list[str] = expression.split(' ')
        operations : list[str] = ['+', '*', '=']
        for token in reversed(token_list):
            self.stack.push(token if token in operations else int(token))

    def clear_expression_stack(self) -> None:
        ''' Clears stack. '''
        while self.stack.pop():
            continue
        self.assertEqual(self.stack.size(), 0)

    def test_on_empty_expression(self) -> None:
        ''' Tests function on empty expression. "None" Expected. '''
        self.assertIsNone(eval_postfix(self.stack))

    def test_on_singleval_expression(self) -> None:
        ''' Tests function on expression <value>=
            Same value must returned. '''
        self.push_postfix_expression_to_stack('5 =')
        self.assertEqual(eval_postfix(self.stack), 5)

    def test_on_predefined_expressions(self) -> None:
        ''' Tests function on predefined correct expressions.
            Expected value must be same as in the result_list. '''
        exression_result_dict : dict[str, int] = {
            '1 2 + 3 * =': 9,
            '8 2 + 5 * 9 + =': 59
        }
        for expression, result in exression_result_dict.items():
            self.push_postfix_expression_to_stack(expression)
            with self.subTest(expression = expression):
                self.assertEqual(eval_postfix(self.stack), result)
            self.clear_expression_stack()

unittest.main()
