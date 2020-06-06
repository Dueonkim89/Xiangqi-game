import unittest
from XiangqiGame import XiangqiGame

# 8 instances of the game board
test = XiangqiGame()
test2 = XiangqiGame()
test3 = XiangqiGame()
test4 = XiangqiGame()
test5 = XiangqiGame()
test6 = XiangqiGame()
test7 = XiangqiGame()
test8 = XiangqiGame()
test9 = XiangqiGame()

class ThirdXiangqiTest(unittest.TestCase):
    def test_case_5(self):
        '''check stalemate'''
        test9.make_move('h3', 'h10')
        test9.make_move('b8', 'b1')
        test9.make_move('a1', 'b1')
        test9.make_move('i10', 'h10')
        test9.make_move('i1', 'i3')
        test9.make_move('a10', 'a8')
        test9.make_move('i3', 'h3')
        test9.make_move('a8', 'b8')
        test9.make_move('h3', 'h8')
        test9.make_move('b8', 'b3')
        test9.make_move('h8', 'h10')
        test9.make_move('b3', 'b1')
        test9.make_move('h10', 'g10')
        test9.make_move('b1', 'c1')
        test9.make_move('g10', 'f10')
        test9.make_move('e10', 'e9')
        test9.make_move('f10', 'd10')
        test9.make_move('c1', 'c4')
        test9.make_move('d10', 'c10')
        test9.make_move('c4', 'e4')
        test9.make_move('d1', 'e2')
        test9.make_move('e4', 'g4')
        test9.make_move('c10', 'b10')
        test9.make_move('g4', 'i4')
        test9.make_move('b10', 'b7')
        test9.make_move('i4', 'i1')
        test9.make_move('b7', 'c7')
        test9.make_move('i1', 'h1')
        test9.make_move('c7', 'e7')
        test9.make_move('e9', 'd9')
        test9.make_move('e7', 'g7')
        test9.make_move('h1', 'g1')
        test9.make_move('g7', 'i7')
        test9.make_move('d9', 'd10')
        test9.make_move('a4', 'a5')
        test9.make_move('d10', 'e10')
        test9.make_move('a5', 'a6')
        test9.make_move('a7', 'a6')
        test9.make_move('i7', 'i6')
        test9.make_move('a6', 'a5')
        test9.make_move('i6', 'i5')
        test9.make_move('a5', 'b5')
        test9.make_move('i5', 'i4')
        test9.make_move('b5', 'c5')
        test9.make_move('i4', 'h4')
        test9.make_move('c5', 'd5')
        test9.make_move('h4', 'i4')
        test9.make_move('g1', 'g4')
        test9.make_move('i4', 'g4')
        test9.make_move('d5', 'c5')
        test9.make_move('g4', 'd4')
        test9.make_move('c5', 'c4')
        test9.make_move('d4', 'd3')
        test9.make_move('c4', 'c3')
        test9.make_move('d3', 'd1')
        test9.make_move('c3', 'c2')
        test9.make_move('d1', 'd2')
        test9.make_move('c2', 'd2')
        print(test9.is_in_check('red'))
        status = test9.get_game_state()
        self.assertEqual(status, 'BLACK_WON')

    def test_case_4(self):
        '''more test'''
        test8.make_move('i4', 'i5')
        test8.make_move('h8', 'f8')
        test8.make_move('g4', 'g5')
        test8.make_move('b8', 'b1')
        test8.make_move('e4', 'e5')
        test8.make_move('b1', 'd1')
        test8.make_move('c4', 'c5')
        test8.make_move('d1', 'f1')
        test8.make_move('a4', 'a5')
        test8.make_move('f1', 'h1')
        test8.make_move('e1', 'e2')
        test8.make_move('a10', 'a8')
        test8.make_move('a5', 'a6')
        test8.make_move('a8', 'b8')
        test8.make_move('a6', 'a7')
        test8.make_move('b8', 'b3')
        test8.make_move('a7', 'b7')
        test8.make_move('i10', 'i9')
        test8.make_move('i5', 'i6')
        test8.make_move('i9', 'f9')
        test8.make_move('b7', 'c7')
        test8.make_move('f8', 'f2')
        test8.make_move('i6', 'i7')
        test8.make_move('f9', 'f3')
        test8.make_move('i1', 'h1')
        test8.make_move('f2', 'i2')
        test8.make_move('e2', 'd2')
        test8.make_move('f10', 'e9')
        test8.make_move('d2', 'd1')
        test8.make_move('f3', 'f1')
        test8.make_move('d1', 'd2')
        test8.make_move('f1', 'g1')
        test8.make_move('h3', 'h7')
        test8.make_move('g1', 'h1')
        test8.make_move('i7', 'i8')
        test8.make_move('h1', 'c1')
        test8.make_move('i8', 'i9')
        test8.make_move('c1', 'a1')
        test8.make_move('i9', 'i10')
        test8.make_move('a1', 'a2')
        test8.make_move('d2', 'd1')
        test8.make_move('b3', 'b1')
        status = test8.get_game_state()
        self.assertEqual(status, 'BLACK_WON')

    def test_case_3(self):
        '''Test for checkmate'''
        test7.make_move('c1', 'e3')
        test7.make_move('h8', 'e8')
        test7.make_move('b1', 'c3')
        test7.make_move('e7', 'e6')
        test7.make_move('h1', 'g3')
        test7.make_move('i10', 'i8')
        test7.make_move('g4', 'g5')
        test7.make_move('i8', 'f8')
        test7.make_move('d1', 'e2')
        test7.make_move('a10', 'a9')
        test7.make_move('b3', 'b10')
        test7.make_move('a9', 'f9')
        test7.make_move('a1', 'd1')
        test7.make_move('f8', 'f1')
        test7.make_move('e2', 'f1')
        test7.make_move('h10', 'g8')
        test7.make_move('d1', 'd10')
        test7.make_move('e10', 'd10')  # False
        test7.make_move('e10', 'e9')
        test7.make_move('e1', 'd1')
        test7.make_move('e8', 'e7')
        test7.make_move('d10', 'd9')
        test7.make_move('e9', 'e8')
        test7.make_move('d9', 'f9')
        test7.make_move('a7', 'a6')
        test7.make_move('h3', 'h8')
        test7.make_move('g8', 'h10')
        test7.make_move('h8', 'b8')
        test7.make_move('i7', 'i6')
        test7.make_move('b8', 'c8')
        test7.make_move('c7', 'c6')
        test7.make_move('b10', 'b8')
        status = test7.get_game_state()
        self.assertEqual(status, 'RED_WON')

    def test_case_2(self):
        '''More tests'''
        test6.make_move('h3', 'e3')
        test6.make_move('e7', 'e6')
        test6.make_move('e4', 'e5')
        test6.make_move('e6', 'e5')
        test6.make_move('b8', 'e8')
        test6.make_move('e5', 'e6')
        test6.make_move('e8', 'e3')
        test6.make_move('c1', 'e3')
        test6.make_move('h10', 'g8')
        test6.make_move('h1', 'g3')
        test6.make_move('b10', 'c8')
        test6.make_move('i1', 'h1')
        test6.make_move('i10', 'h10')
        test6.make_move('h1', 'h7')
        test6.make_move('g7', 'g6')
        test6.make_move('h7', 'g7')
        test6.make_move('g8', 'e9')
        test6.make_move('b1', 'c3')
        test6.make_move('h8', 'g8')
        test6.make_move('g3', 'e4')
        test6.make_move('g8', 'g7')  # False
        test6.make_move('i7', 'i6')
        test6.make_move('e4', 'f6')
        test6.make_move('h10', 'h1')
        test6.make_move('f6', 'g8')
        test6.make_move('e9', 'g8')
        test6.make_move('g7', 'g8')
        test6.make_move('h1', 'g1')
        test6.make_move('e3', 'g1')
        test6.make_move('c8', 'e9')
        test6.make_move('g8', 'g6')
        test6.make_move('a10', 'a8')
        test6.make_move('a1', 'c1')
        test6.make_move('a1', 'c1')
        test6.make_move('a8', 'h8')
        test6.make_move('g4', 'g5')
        test6.make_move('h8', 'h4')
        test6.make_move('g6', 'g7')
        test6.make_move('g10', 'e8')
        test6.make_move('c4', 'c5')
        test6.make_move('h4', 'i4')
        test6.make_move('b3', 'b7')
        test6.make_move('i4', 'a4')
        test6.make_move('c3', 'a4')
        test6.make_move('e9', 'c8')
        test6.make_move('g7', 'c7')
        test6.make_move('a7', 'a6')
        test6.make_move('a4', 'b6')
        test6.make_move('d10', 'e9')
        test6.make_move('c7', 'c8')
        test6.make_move('e10', 'd10')
        test6.make_move('b7', 'b10')
        test6.make_move('d10', 'd9')
        test6.make_move('c8', 'c9')
        test6.make_move('d9', 'd8')
        test6.make_move('b10', 'b8')
        test6.make_move('e8', 'c6')
        test6.make_move('b6', 'c8')
        status = test6.get_game_state()
        self.assertEqual(status, 'RED_WON')

    def test_case(self):
        '''Test result'''
        test5.make_move('h3', 'h10')
        test5.make_move('i10', 'h10')
        test5.make_move('b3', 'b10')
        test5.make_move('a10', 'b10')
        test5.make_move('h1', 'g3')
        test5.make_move('h8', 'e8')
        test5.make_move('e4', 'e5')
        test5.make_move('e8', 'e5')
        test5.make_move('b1', 'c3')
        test5.make_move('b8', 'b6')
        test5.make_move('g1', 'e3')
        test5.make_move('g4', 'g5')
        test5.make_move('b6', 'e6')
        status = test5.get_game_state()
        self.assertEqual(status, 'BLACK_WON')

class SecondXiangqi(unittest.TestCase):
    '''More unit tests for second instance'''
    def test_1(self):
        '''illegal red cannon movement'''
        status = test2.make_move('b3', 'b8')
        self.assertEqual(status, False)

    def test_2(self):
        '''red cannon takes horse and dies'''
        test3.make_move('b3', 'b10')
        status = test3.make_move('a10', 'b10')
        self.assertEqual(status, True)

    def test_3(self):
        '''move red horse, black cannon takes horse and dies'''
        test3.make_move('b1', 'c3')
        test3.make_move('h8', 'h1')
        status = test3.make_move('i1', 'h1')
        self.assertEqual(status, True)

    def test_4(self):
        '''black advisor moves out of place'''
        status = test3.make_move('f10', 'g9')
        self.assertEqual(status, False)


class TestXiangqi(unittest.TestCase):
    """Contains unit tests for the Xiangqi object"""
    def test_red_horse_blocked(self):
        '''Test if false is returned'''
        status = test.make_move('b1', 'd2')
        self.assertEqual(status, False)

    def test_out_of_bounds_for_nonexistant_column(self):
        '''Test if false is returned.'''
        status = test.make_move('e4', 't5')
        self.assertEqual(status, False)

    def test_out_of_bounds_for_nonexistant_row(self):
        '''Test if false is returned.'''
        status = test.make_move('a11', 'a10')
        self.assertEqual(status, False)

    def test_out_of_bounds_for_nonexistant_row_2(self):
        '''Test if false is returned.'''
        status = test.make_move('a10', 'a12')
        self.assertEqual(status, False)

    def test_out_of_bounds_for_nonexistant_column_2(self):
        '''Test if false is returned.'''
        status = test.make_move('z4', 'g5')
        self.assertEqual(status, False)

    def test_empty_coordinates(self):
        '''Test if false is returned.'''
        status = test.make_move('b7', 'b6')
        self.assertEqual(status, False)

    def test_red_solider_illegal_move(self):
        '''Test if false'''
        status = test.make_move('i4', 'i3')
        self.assertEqual(status, False)

    def test_black_solider_illegal_move(self):
        '''Test if True'''
        test.make_move('i4', 'i5')
        status = test.make_move('e7', 'e8')
        self.assertEqual(status, False)

    def test_black_player_going_first(self):
        ''' Test if false is returned.'''
        status = test.make_move('a7', 'a6')
        self.assertEqual(status, False)


if __name__ == '__main__':
    unittest.main()