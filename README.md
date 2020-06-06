# Xiangqi-game

Red is the starting player.

Locations on the board will be specified using "algebraic notation", with columns labeled a-i and rows labeled 1-10, with row 
1 being the Red side and row 10 the Black side.

Game is over when general has been checkmated or stalemated.

The pieces are: Solider, Cannon, Rook, Horse, Elephant, General & Adviser.

Here is an example of how to play.

```
game = XiangqiGame()
move_result = game.make_move('c1', 'e3')
black_in_check = game.is_in_check('black')
game.make_move('e7', 'e6')
state = game.get_game_state()
```
