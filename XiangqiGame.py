# Red player will start first.

import os


class Player:
    '''Represents the 2 players black and red'''

    def __init__(self, color):
        '''Initialize the needed pieces and the color'''
        self._color = color
        self._soldier_list = [Soldier(self._color, 'Soldier') for x in range(5)]
        self._cannon_list = [Cannon(self._color, 'Cannon') for x in range(2)]
        self._rook_list = [Rook(self._color, 'Rook') for x in range(2)]
        self._horse_list = [Horse(self._color, 'Horse') for x in range(2)]
        self._elephant_list = [Elephant(self._color, 'Elephant') for x in range(2)]
        self._adviser_list = [Adviser(self._color, 'Adviser') for x in range(2)]
        self._general_list = [General(self._color, 'General') for x in range(1)]

    def get_solider_pieces(self):
        '''Return the list of 5 soldiers'''
        return self._soldier_list

    def get_cannon_pieces(self):
        '''Return the list of 2 cannons'''
        return self._cannon_list

    def get_general_piece(self):
        '''Return the list of general'''
        return self._general_list

    def get_adviser_pieces(self):
        '''Return the list of 2 advisors'''
        return self._adviser_list

    def get_rook_pieces(self):
        '''Return the list of 2 rooks'''
        return self._rook_list

    def get_elephant_pieces(self):
        '''Return the list of 2 elephants'''
        return self._elephant_list

    def get_horse_pieces(self):
        '''Return the list of 2 elephants'''
        return self._horse_list


class Piece:
    '''Represents the pieces on the board'''

    def __init__(self, color, name):
        '''Class for the piece. Private data includes player_color,
        piece_name, river, coordinates, fortress, letter_to_number dict,
        board'''
        self._color = color
        self._piece_name = name
        self._coordinates = None
        self._letter_to_number_dict = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8
        }
        self._number_to_letter_dict = {
            0: 'a', 1: 'b', 2: 'c', 3: 'd',
            4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'
        }
        self._board = XiangqiGame.draw_board()

        if self._color == 'Red':
            self._river = 5
            self._fortress = ['d1', 'e1', 'f1', 'd2', 'e2', 'f2', 'd3', 'e3', 'f3']
        else:
            self._river = 6
            self._fortress = ['d8', 'e8', 'f8', 'd9', 'e9', 'f9', 'd10', 'e10', 'f10']

    def __repr__(self):
        '''Print piece object as string for clarity and debugging'''
        return '\'' + self._color[0] + self._piece_name[0] + '\''

    def set_coordinates(self, position):
        '''Set the coordinates of the piece'''
        self._coordinates = position

    def get_coordinates(self):
        '''Get the coordinates of the piece'''
        return self._coordinates

    def get_river_position(self):
        '''Get the river position'''
        return self._river

    def get_color(self):
        '''return the color of the piece'''
        return self._color

    def get_piece_name(self):
        '''return name of the piece'''
        return self._piece_name

    def _is_blocked(self, piece_name, current_coordinates, destination, board, color):
        '''Remove all blocked coordinates for Horse and Elephant'''

        # current row & column, destination row & column
        current_row = int(current_coordinates[1:])
        current_column = self._letter_to_number_dict[current_coordinates[0]]
        destination_row = int(destination[1:])
        destination_column = self._letter_to_number_dict[destination[0]]

        # return same color
        if board[destination_row][destination_column] != '..':
            return board[destination_row][destination_column].get_color() == color

        if piece_name == 'Horse':
            # moving down
            if destination_row > current_row:
                # moving 1 left or 1 right
                if current_column + 1 == destination_column or current_column - 1 == destination_column:
                    # midpoint is 1 row down, same column
                    mid_row = current_row + 1
                    mid_column = current_column
                # moving 2 left
                elif current_column - 2 == destination_column:
                    # midpoint is same row, 1 column left
                    mid_row = current_row
                    mid_column = current_column - 1
                # moving 2 right
                elif current_column + 2 == destination_column:
                    # midpoint is same row, 1 column right
                    mid_row = current_row
                    mid_column = current_column + 1
            # moving up
            else:
                # moving 1 left or right
                if current_column + 1 == destination_column or current_column - 1 == destination_column:
                    # midpoint is same column, 1 row up
                    mid_row = current_row - 1
                    mid_column = current_column
                # moving 2 left
                elif current_column - 2 == destination_column:
                    # midpoint is same row, 1 column left
                    mid_row = current_row
                    mid_column = current_column - 1
                # moving 2 right
                elif current_column + 2 == destination_column:
                    # midpoint is same row, 1 column right
                    mid_row = current_row
                    mid_column = current_column + 1

            # return boolean value of coordinates equaling empty space
            return board[mid_row][mid_column] != '..'

        # remove blocked coordinates for elephant
        elif piece_name == 'Elephant':
            # moving up
            if destination_row < current_row:
                mid_row = current_row - 1
                # moving left
                if destination_column < current_column:
                    mid_column = current_column - 1
                # moving right
                else:
                    mid_column = current_column + 1
            # moving down
            else:
                mid_row = current_row + 1
                # moving left
                if destination_column < current_column:
                    mid_column = current_column - 1
                # moving right
                else:
                    mid_column = current_column + 1

            # return boolean value of coordinates equaling empty space
            return board[mid_row][mid_column] != '..'

    def _remove_out_of_bounds_coordinates(self, list_of_moves, board, color):
        '''Filter out out of bounds coordinates from list of moves'''
        filtered_list = []
        for move in list_of_moves:
            # negative sign, continue
            if '-' in move:
                continue
            row = int(move[1:])
            column = int(move[0])
            try:
                col = self._number_to_letter_dict[column]
            except KeyError:
                continue
            try:
                self._board[row]
            except KeyError:
                continue

            # if coords has same color piece, continue
            if board[row][column] != '..' and board[row][column].get_color() == color:
                continue

            coord = col + str(row)
            # if piece is adviser or general, make sure along the fortress
            if self._piece_name == 'General' or self._piece_name == 'Adviser':
                if coord in self._fortress:
                    filtered_list.append(coord)
            else:
                filtered_list.append(coord)

        return filtered_list


class Horse(Piece):
    def __init__(self, color, name):
        '''initialize the name and color of the Cannon'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Can move 2 in row or column and 1 in row or column afterwards.
        Can move in 8 ways if in center of board.'''

        # get old position, current_row and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()

        # list to hold movements, column
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]

        # store variables for the positions needed
        up_two = current_row + 2
        down_two = current_row - 2
        up_one = current_row + 1
        down_one = current_row - 1
        left_two = column - 2
        right_two = column + 2
        right_one = column + 1
        left_one = column - 1

        # make sure all variables for rows above are not less than 1 and greater than 10
        # make sure all variables for columns are not less than 0 and greater than 8
        if 1 <= up_two <= 10:
            if 0 <= right_one <= 8:
                # add first movement, up 2, 1 right
                movement_list.append(str(right_one) + str(up_two))
            if 0 <= left_one <= 8:
                # add second movement, up 2, 1 left.
                movement_list.append(str(left_one) + str(up_two))
        if 1 <= down_two <= 10:
            if 0 <= left_one <= 8:
                # add 3rd movement, down 2, 1 left
                movement_list.append(str(left_one) + str(down_two))
            if 0 <= right_one <= 8:
                # add 4th movement, down 2, 1 right
                movement_list.append(str(right_one) + str(down_two))
        if 1 <= down_one <= 10:
            if 0 <= right_two <= 8:
                # add 5th movement, 2 right, 1 down
                movement_list.append(str(right_two) + str(down_one))
            if 0 <= left_two <= 8:
                # add 6th movement, 2 left, 1 down
                movement_list.append(str(left_two) + str(down_one))
        if 1 <= up_one <= 10:
            if 0 <= right_two <= 8:
                # add 7th movement, 2 right, 1 up
                movement_list.append(str(right_two) + str(up_one))
            if 0 <= left_two <= 8:
                # add 8th movement, 2 left, 1 up
                movement_list.append(str(left_two) + str(up_one))

        # filter out of bounds.
        filtered_list = self._remove_out_of_bounds_coordinates(movement_list, board, color)

        # print('line 273: horse ML', movement_list)
        # print('line 274: horse filtered', filtered_list, old_position)

        # nonblocked movements
        nonblocked_list = []

        # remove blocked movements. pass in current_coordinates, name of piece, list of moves
        for move in filtered_list:
            if not self._is_blocked(self.get_piece_name(), old_position, move, board, color):
                nonblocked_list.append(move)

        # print('line 285 horse no_block', nonblocked_list, old_position)

        # if new position is not provided, return the list of filtered & blocked movements
        if new_position is None:
            return nonblocked_list

        # return True if movement possible, else False
        if new_position in nonblocked_list:
            return True

        return False


class Cannon(Piece):
    '''Inherits from piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the Cannon'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Can move N spaces horizontally or vertically as long as not blocked.
        Can also jump over to closest enemy if behind any piece.'''

        # get old position, current_row and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()

        # list to hold movements, column, piece_in_front
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]
        piece_in_front = False

        # loop from current column + 1, all the way to the right side
        for x in range(column + 1, 9):
            # current piece at grid and coordinates
            grid_piece = board[current_row][x]
            current_coordinates = self._number_to_letter_dict[x] + str(current_row)
            # if piece in front and opposing player
            if piece_in_front and grid_piece != '..' and grid_piece.get_color() != color:
                movement_list.append(current_coordinates)
                break
            # if empty and its before piece_in_front, append to movement_list
            elif grid_piece == '..' and piece_in_front is False:
                movement_list.append(current_coordinates)
            # else, there is a piece in front of the cannon
            else:
                # set boolean to true
                piece_in_front = True

        # reset the piece_in_front
        piece_in_front = False

        # loop from current column - 1, all the way to the left side
        for w in range(column - 1, -1, -1):
            # current piece at grid and coordinates
            try:
                grid_piece = board[current_row][w]
                current_coordinates = self._number_to_letter_dict[w] + str(current_row)
                # if piece in front and opposing player
                if piece_in_front and grid_piece != '..' and grid_piece.get_color() != color:
                    movement_list.append(current_coordinates)
                    break
                # if empty and its before piece_in_front, append to movement_list
                elif grid_piece == '..' and piece_in_front is False:
                    movement_list.append(current_coordinates)
                # else, there is a piece in front of the cannon
                else:
                    # set boolean to true
                    piece_in_front = True
            except KeyError:
                break

        # reset the piece_in_front, hold column in alphabet form
        piece_in_front = False
        col = self._number_to_letter_dict[column]

        # loop from current row - 1, all the way to the bottom
        for y in range(current_row + 1, 11):
            # current piece at grid and coordinates
            grid_piece = board[y][column]
            current_coordinates = col + str(y)
            # if piece in front and opposing player
            if piece_in_front and grid_piece != '..' and grid_piece.get_color() != color:
                movement_list.append(current_coordinates)
                break
            # if empty and its before piece_in_front, append to movement_list
            elif grid_piece == '..' and piece_in_front is False:
                movement_list.append(current_coordinates)
            # else, there is a piece in front of the cannon
            else:
                # set boolean to true
                piece_in_front = True

        # reset the piece_in_front
        piece_in_front = False

        # loop from current row  -1, all the way to top
        for z in range(current_row -1, -1, -1):
            try:
                # current piece at grid and coordinates
                grid_piece = board[z][column]
                current_coordinates = col + str(z)
                # if piece in front and opposing player
                if piece_in_front and grid_piece != '..' and grid_piece.get_color() != color:
                    movement_list.append(current_coordinates)
                    break
                # if empty and its before piece_in_front, append to movement_list
                elif grid_piece == '..' and piece_in_front is False:
                    movement_list.append(current_coordinates)
                # else, there is a piece in front of the cannon
                else:
                    # set boolean to true
                    piece_in_front = True
            except KeyError:
                break

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return movement_list

        # return True if movement possible, else False
        if new_position in movement_list:
            return True

        return False


class Rook(Piece):
    '''Inherits from piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the Rook'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Can move N spaces horizontally or vertically as long as not blocked'''

        # get old position, current_row and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()

        # list to hold movements, column
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]

        # loop from current column + 1, all the way to the right side
        for x in range(column + 1, 9):
            # current piece at grid and coordinates
            grid_piece = board[current_row][x]
            current_coordinates = self._number_to_letter_dict[x] + str(current_row)
            # if empty, append to movement_list
            if grid_piece == '..':
                movement_list.append(current_coordinates)
            else:
                # if that piece in grid is not same color.
                if grid_piece.get_color() != color:
                    # add to movement_list and break
                    movement_list.append(current_coordinates)
                    break
                else:
                    break

        # loop from current column - 1,  all the way to the left
        for y in range(column - 1, -1, -1):
            try:
                # current piece at grid and coordinates
                grid_piece = board[current_row][y]
                current_coordinates = self._number_to_letter_dict[y] + str(current_row)
                # if empty, append to movement_list
                if grid_piece == '..':
                    movement_list.append(current_coordinates)
                else:
                    # if that piece in grid is not same color.
                    if grid_piece.get_color() != color:
                        # add to movement_list and break
                        movement_list.append(current_coordinates)
                        break
                    else:
                        break
            except KeyError:
                break

        # loop from current row +1, all the way to the bottom
        for z in range(current_row + 1, 11):
            grid_piece = board[z][column]
            current_coordinates = self._number_to_letter_dict[column] + str(z)
            # if empty, append to movement_list
            if grid_piece == '..':
                movement_list.append(current_coordinates)
            else:
                # if that piece in grid is not same color.
                if grid_piece.get_color() != color:
                    # add to movement_list and break
                    movement_list.append(current_coordinates)
                    break
                else:
                    break

        # loop from current row -1,  all the way to the top.
        for w in range(current_row - 1, -1, -1):
            try:
                grid_piece = board[w][column]
                current_coordinates = self._number_to_letter_dict[column] + str(w)
            # if empty, append to movement_list
                if grid_piece == '..':
                    movement_list.append(current_coordinates)
                else:
                    # if that piece in grid is not same color.
                    if grid_piece.get_color() != color:
                        # add to movement_list and break
                        movement_list.append(current_coordinates)
                        break
                    else:
                        break
            except KeyError:
                break

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return movement_list

        # return True if movement possible, else False
        if new_position in movement_list:
            return True

        return False


class Elephant(Piece):
    '''Inherits from piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the Elephant'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Moves 2 space diagonally left or right. CANNOT cross river.'''

        # get old position, current_row, river and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()
        river = self.get_river_position()

        # list to hold movements, column, left, right
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]
        left = column - 2
        right = column + 2

        # come up with movements for red and black elephant
        if color == 'Red':
            # top and bottom for red
            top = current_row + 2
            bottom = current_row - 2
        else:
            # top and bottom for black
            top = current_row - 2
            bottom = current_row + 2

        # if at river, go south left or south right only
        if current_row == river:
            movement_list.append(str(left) + str(bottom))
            movement_list.append(str(right) + str(bottom))
        # at left most column, north right or south right
        elif column == 0:
            movement_list.append(str(right) + str(top))
            movement_list.append(str(right) + str(bottom))
        # at right most column, south left or north left
        elif column == 8:
            movement_list.append(str(left) + str(bottom))
            movement_list.append(str(left) + str(top))
        # else, move  north left, north right, south left, south right
        else:
            movement_list.append(str(left) + str(bottom))
            movement_list.append(str(right) + str(bottom))
            movement_list.append(str(left) + str(top))
            movement_list.append(str(right) + str(top))

        # filter out out of bounds movement
        filtered_result = self._remove_out_of_bounds_coordinates(movement_list, board, color)

        # list for nonblocked movements
        nonblocked_movements = []

        # print('line 570, filtered elephant moves', filtered_result)

        # remove blocked coordinates
        for move in filtered_result:
            if not self._is_blocked(self.get_piece_name(), old_position, move, board, color):
                nonblocked_movements.append(move)

        # print('line 577, elephant nonblocked moves', nonblocked_movements, old_position)

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return nonblocked_movements

        # return True if movement possible, else False
        if new_position in nonblocked_movements:
            return True

        return False


class Adviser(Piece):
    '''Inherits from piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the Adviser'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Moves 1 space diagonally left or right along the fortress'''

        # get old position, current_row, and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()

        # list to hold movements, column, left, right
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]
        left = column - 1
        right = column + 1

        # come up with movements for red adviser and black adviser
        if color == 'Red':
            # top and bottom for red
            top = current_row + 1
            bottom = current_row - 1
        else:
            # top and bottom for black
            top = current_row - 1
            bottom = current_row + 1

        # north & south left diagonal, north & south right diagonal
        movement_list.append(str(left) + str(top))
        movement_list.append(str(left) + str(bottom))
        movement_list.append(str(right) + str(top))
        movement_list.append(str(right) + str(bottom))

        # filter out out of bounds movement
        filtered_result = self._remove_out_of_bounds_coordinates(movement_list, board, color)

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return filtered_result

        # return True if movement possible, else False
        if new_position in filtered_result:
            return True

        return False


class General(Piece):
    '''Child class of Piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the General'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''General can only move left, up right, or down along the 9
            points of the fortress.'''

        # get old position, current_row, and color
        old_position = self.get_coordinates()
        current_row = int(old_position[1:])
        color = self.get_color()

        # list to hold movements, column, left, right
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]
        left = column - 1
        right = column + 1

        # left, right, up and down movements
        movement_list.append(str(left) + str(current_row))
        movement_list.append(str(right) + str(current_row))
        movement_list.append(str(column) + str(current_row + 1))
        movement_list.append(str(column) + str(current_row - 1))

        # filter out out of bounds movement
        filtered_result = self._remove_out_of_bounds_coordinates(movement_list, board, color)

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return filtered_result

        # return True if movement possible, else False
        if new_position in filtered_result:
            return True

        return False


class Soldier(Piece):
    '''Child class of Piece'''
    def __init__(self, color, name):
        '''initialize the name and color of the Soldier'''
        super().__init__(color, name)

    def move(self, new_position, board=None):
        '''Move the solider. Can only move 1 space forward until river is
        crossed. Then it can move left, right and up.'''
        # get old position, current_row, river, and color
        old_position = self.get_coordinates()
        color = self.get_color()
        river = self.get_river_position()
        current_row = int(old_position[1:])

        # list to hold movements, column, left, right
        movement_list = []
        column = self._letter_to_number_dict[old_position[0]]
        left = column - 1
        right = column + 1

        # if black player, come up with possible movements
        if color == 'Black':
            # top for black
            top = current_row - 1
            # if at top, only move left and right
            if current_row == 1:
                movement_list.append(str(left)+str(current_row))
                movement_list.append(str(right)+str(current_row))
            # elif not at top and past river, calculate top, left, right movements
            elif current_row != 1 and current_row < river:
                movement_list.append(str(left)+str(current_row))
                movement_list.append(str(right)+str(current_row))
                movement_list.append(str(column) + str(top))
            # else, calculate top movements only
            else:
                movement_list.append(str(column) + str(top))
        # red player, come up with possible movements
        else:
            # top for red
            top = current_row + 1
            # if at top, only move left and right
            if current_row == 10:
                movement_list.append(str(left)+str(current_row))
                movement_list.append(str(right)+str(current_row))
            # elif not at top and past river, calculate top, left, right movements
            elif current_row != 10 and current_row > river:
                movement_list.append(str(left)+str(current_row))
                movement_list.append(str(right)+str(current_row))
                movement_list.append(str(column) + str(top))
            # else, calculate top movements only
            else:
                movement_list.append(str(column) + str(top))

        # filter out out of bounds movement
        filtered_result = self._remove_out_of_bounds_coordinates(movement_list, board, color)

        # if new position is not provided, return the list of filtered movements
        if new_position is None:
            return filtered_result

        # return True if movement possible, else False
        if new_position in filtered_result:
            return True

        return False


class XiangqiGame:
    '''Class for the game Xiangqi with private data and methods.'''

    def __init__(self):
        '''Set the board for the game, letter to number dict, game_state,
        player_turn, red & black piece on board, number to letter dict,
        red & black general, red & black player'''
        self._red_player = Player('Red')
        self._black_player = Player('Black')
        self._black_pieces_on_board = []
        self._black_general = None
        self._red_general = None
        self._red_pieces_on_board = []
        self._player_turn = 'Red'
        self._board = XiangqiGame.draw_board()
        self._game_state = 'UNFINISHED'
        self._letter_to_number_dict = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8
        }
        self._number_to_letter_dict = {
            0: 'a', 1: 'b', 2: 'c', 3: 'd',
            4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i'
        }
        self._set_pieces_on_board()

    def _draw_the_board(self):
        '''draw the board'''
        # clear previous board and draw new board.
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = os.system('clear')

        # draw the board
        print('     a     b     c     d     e     f     g     h     i')
        for i, key in enumerate(self._board):
            print(i + 1, self._board[key])

    def _update_pieces_for_player(self, data, player_color):
        '''update pieces on board for the provided player'''
        if player_color == 'Red':
            # if list is provided, overwrite current pieces
            if type(data) is list:
                self._red_pieces_on_board = data
            # else, append to the current piece
            else:
                self._red_pieces_on_board.append(data)
        else:
            if type(data) is list:
                self._black_pieces_on_board = data
            else:
                self._black_pieces_on_board.append(data)

    @staticmethod
    def draw_board():
        '''Method to draw board, will be used by other classes'''
        board = {}
        for row in range(1, 11):
            board[row] = ['..' for x in range(9)]
        return board

    def _set_pieces_on_board(self):
        '''Set red and black player pieces on the board'''

        # dict to hold the starting position of the pieces.
        initial_position = {
            'black_soldiers': ['a7', 'c7', 'e7', 'g7', 'i7'],
            'red_soldiers': ['a4', 'c4', 'e4', 'g4', 'i4'],
            'red_general': ['e1'],
            'black_general': ['e10'],
            'red_adviser': ['d1', 'f1'],
            'black_adviser': ['d10', 'f10'],
            'red_elephant': ['c1', 'g1'],
            'black_elephant': ['c10', 'g10'],
            'red_rook': ['a1', 'i1'],
            'black_rook': ['a10', 'i10'],
            'red_cannon': ['b3', 'h3'],
            'black_cannon': ['b8', 'h8'],
            'red_horse': ['b1', 'h1'],
            'black_horse': ['b10', 'h10']
        }

        # dict to hold red, black pieces
        pieces_dict = {
            'red_soldiers': self._red_player.get_solider_pieces(),
            'black_soldiers': self._black_player.get_solider_pieces(),
            'red_general': self._red_player.get_general_piece(),
            'black_general': self._black_player.get_general_piece(),
            'red_adviser': self._red_player.get_adviser_pieces(),
            'black_adviser': self._black_player.get_adviser_pieces(),
            'red_elephant': self._red_player.get_elephant_pieces(),
            'black_elephant': self._black_player.get_elephant_pieces(),
            'red_rook': self._red_player.get_rook_pieces(),
            'black_rook': self._black_player.get_rook_pieces(),
            'red_cannon': self._red_player.get_cannon_pieces(),
            'black_cannon': self._black_player.get_cannon_pieces(),
            'red_horse': self._red_player.get_horse_pieces(),
            'black_horse': self._black_player.get_horse_pieces()
        }

        # store the red & black general as data members
        self._black_general = pieces_dict['black_general'][0]
        self._red_general = pieces_dict['red_general'][0]

        # loop through the keys and set the pieces on board.
        for keys in initial_position:
            # for each key, set coordinates on board and for the piece itself, update pieces on the board.
            for index, k in enumerate(initial_position[keys]):
                self._set_piece_to_coordinates(k, pieces_dict[keys][index])
                pieces_dict[keys][index].set_coordinates(k)
                if 'red' in keys:
                    self._red_pieces_on_board.append(pieces_dict[keys][index])
                else:
                    self._black_pieces_on_board.append(pieces_dict[keys][index])

    def _set_player_turn(self):
        '''Set the next players turn'''
        if self._player_turn == 'Red':
            self._player_turn = 'Black'
            return True
        self._player_turn = 'Red'

    def get_game_state(self):
        '''Public method will return the state of the game which will be either:
            UNFINISHED, RED_WON or BLACK_WON
        '''
        return self._game_state

    def _remove_occupied_moves(self, list_of_moves, color):
        '''private method to remove moves occupied by same color piece'''
        # list to hold non blocked movements
        filtered_move_list = []

        # remove moves occupied by same color piece
        for m in list_of_moves:
            piece = self.get_piece_from_coordinates(m)

            if piece == '..' or piece.get_color() != color:
                filtered_move_list.append(m)

        # return the list
        return filtered_move_list

    def is_in_check(self, player_color):
        '''Determine if player in argument is in check'''
        # get general coordinates and players pieces
        if player_color == 'red':
            general_coordinates = self._red_general.get_coordinates()
            opposing_player_pieces = self._black_pieces_on_board
        else:
            general_coordinates = self._black_general.get_coordinates()
            opposing_player_pieces = self._red_pieces_on_board

        # set to hold the opposing players movements
        opposing_player_movements = set()

        # loop through and get all the movements
        for pieces in opposing_player_pieces:
            # list of moves
            move_list = pieces.move(None, self._board)

            # loop through the move_list and add to set
            for move in move_list:
                opposing_player_movements.add(move)

        # if any of the movements is the coordinates of general or flying general, return True
        if general_coordinates in opposing_player_movements or self._flying_general():
            return True
        # else return False
        return False

    @staticmethod
    def is_out_of_bounds(coordinate, board, letter_decoder):
        '''Static method to be used by other classes to determine if
        movement is out of bounds'''

        # if row or column doesnt exist on board, return True, else return False
        try:
            board[int(coordinate[1:])][letter_decoder[coordinate[0]]]
        except KeyError:
            return True
        except IndexError:
            return True

        return False

    def get_pieces_for_player(self, color):
        '''Method to get the pieces for provided player'''
        if color == 'Red':
            return self._red_pieces_on_board
        return self._black_pieces_on_board

    def _game_over(self):
        '''Determine if game is over'''
        # get opposing players pieces on the board
        if self._player_turn == "Red":
            pieces = self.get_pieces_for_player('Black')
            player_to_check = 'black'
        else:
            pieces = self.get_pieces_for_player('Red')
            player_to_check = 'red'

        # list to hold the data for the pieces
        pieces_data_list = []

        # loop through the pieces and create a dict with the relevant info
        for piece in pieces:
            info = {}
            info['name'] = piece.get_color() + ' ' + piece.get_piece_name()
            info['start_position'] = piece.get_coordinates()
            info['movements'] = piece.move(None, self._board)
            info['piece'] = piece
            pieces_data_list.append(info)

        # loop through the gathered data
        for pcs in pieces_data_list:
            # loop through the movements of each piece
            for move in pcs['movements']:
                # get the piece at the movement
                pc_at_destination = self.get_piece_from_coordinates(move)

                # move piece to the new coordinates and place on board
                self._set_piece_to_coordinates(pcs['start_position'], '..')
                self._set_piece_to_coordinates(move, pcs['piece'])
                pcs['piece'].set_coordinates(move)

                # if color of p.a.d is current player, update the list of pieces on board
                if pc_at_destination != '..' and pc_at_destination.get_color() == self._player_turn:
                    # update that players list to remove the p.a.d
                    updated_pieces = [piece for piece in self.get_pieces_for_player(self._player_turn) if piece is not pc_at_destination]
                    self._update_pieces_for_player(updated_pieces, self._player_turn)

                # see if in check
                if self.is_in_check(player_to_check):
                    # set piece back to start_position, piece back to original coordinates
                    self._set_piece_to_coordinates(pcs['start_position'], pcs['piece'])
                    pcs['piece'].set_coordinates(pcs['start_position'])
                    # set p.a.d back to move coordinates
                    self._set_piece_to_coordinates(move, pc_at_destination)
                    # update that players list to append p.a.d if it was opponent
                    if pc_at_destination != '..' and pc_at_destination.get_color() == self._player_turn:
                        self._update_pieces_for_player(pc_at_destination, self._player_turn)

                else:
                    # same as if in check, except return False at end
                    self._set_piece_to_coordinates(pcs['start_position'], pcs['piece'])
                    pcs['piece'].set_coordinates(pcs['start_position'])
                    self._set_piece_to_coordinates(move, pc_at_destination)
                    if pc_at_destination != '..' and pc_at_destination.get_color() == self._player_turn:
                        self._update_pieces_for_player(pc_at_destination, self._player_turn)
                    return False

        # all moves lead to a check, return True
        return True

    def _illegal_move(self):
        '''determine if move is illegal'''
        # if generals can fly or current player is now in check, return True
        if self._flying_general() or self.is_in_check(self._player_turn.lower()):
            return True

    def _flying_general(self):
        '''check if the generals can do the fly move'''
        # get column & row of red and black general
        red_general_column = self._red_general.get_coordinates()[0]
        black_general_column = self._black_general.get_coordinates()[0]
        red_general_row = int(self._red_general.get_coordinates()[1:])
        black_general_row = int(self._black_general.get_coordinates()[1:])

        # if same column, return false if a piece is in between
        if red_general_column == black_general_column:
            # loop through the rows
            for rows in range(red_general_row + 1, black_general_row):
                # if row and column contains a piece, return False
                if self.get_piece_from_coordinates(red_general_column + str(rows)) != '..':
                    return False

            # no piece in between, return True
            return True

        # not same column, return False
        return False

    def make_move(self, current_position, new_position):
        '''Move the piece on the board if possible.'''

        # game already won, return False
        if self.get_game_state() != 'UNFINISHED':
            print('Game over', self._game_state)
            return False

        # if current or new position is out of bounds, return false.
        if XiangqiGame.is_out_of_bounds(current_position, self._board, self._letter_to_number_dict) or \
                XiangqiGame.is_out_of_bounds(new_position, self._board, self._letter_to_number_dict):
            return False

        # get current player, current piece
        current_player = self._player_turn
        current_piece = self.get_piece_from_coordinates(current_position)

        # if current coordinate is empty, return False
        if current_piece == '..':
            return False

        # new_coordinate, name of piece, color
        new_coordinate = self.get_piece_from_coordinates(new_position)
        name = current_piece.get_piece_name()
        color = current_piece.get_color()

        # if color on the piece doesnt match current player, return False
        if color != current_player:
            return False

        # if piece at new_position is same color, return False
        if new_coordinate != '..' and new_coordinate.get_color() == current_player:
            return False

        # if piece can be moved
        if current_piece.move(new_position, self._board):
            # get opponent pieces on board
            if current_player == 'Red':
                opponent_color = 'Black'
                opponent_pieces = self._black_pieces_on_board
            else:
                opponent_color = 'Red'
                opponent_pieces = self._red_pieces_on_board

            # update new and old coordinates on board and for the piece
            self._set_piece_to_coordinates(current_position, '..')
            self._set_piece_to_coordinates(new_position, current_piece)
            current_piece.set_coordinates(new_position)

            # if new_position contains opponent piece update opponents pieces
            if new_coordinate != '..' and new_coordinate.get_color() != current_player:
                updated_pieces_list = [piece for piece in opponent_pieces if piece is not new_coordinate]
                self._update_pieces_for_player(updated_pieces_list, opponent_color)

            # check if illegal move.
            if self._illegal_move():
                print('illegal move. try another move.')
                # reset the coordinates back to the way it was, append piece back to opponents list
                self._set_piece_to_coordinates(current_position, current_piece)
                self._set_piece_to_coordinates(new_position, new_coordinate)
                current_piece.set_coordinates(current_position)
                if new_coordinate != '..' and new_coordinate.get_color() != current_player:
                    self._update_pieces_for_player(new_coordinate, opponent_color)
                return False

            # check if game is over for opposing player
            if self._game_over():
                if self._player_turn == 'Red':
                    self._game_state = 'RED_WON'
                else:
                    self._game_state = 'BLACK_WON'

            # toggle player and return True
            self._set_player_turn()
            self._draw_the_board()
            return True

        # move cannot be made, return False
        return False

    def get_piece_from_coordinates(self, coordinate):
        '''Get the proper coordinate on board.'''
        # variable for row and column, return the coordinate on board
        row = int(coordinate[1:])
        column = self._letter_to_number_dict[coordinate[0]]
        return self._board[row][column]

    def _set_piece_to_coordinates(self, coordinate, piece):
        '''Set the piece to the coordinate on the board.'''
        # variable for row and column, set the piece to the coordinate
        row = int(coordinate[1:])
        column = self._letter_to_number_dict[coordinate[0]]
        self._board[row][column] = piece


test = XiangqiGame()
test.make_move('c1', 'e3')
test.make_move('e7', 'e6')

'''
print('     a     b     c     d     e     f     g     h     i')
for i, key in enumerate(test._board):
    print(i + 1, test._board[key])
'''