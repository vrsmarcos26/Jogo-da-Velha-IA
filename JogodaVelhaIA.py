    
# JOGO DA VELHA COM IA

from functools import partial
from typing import List, Tuple, Union

import numpy as np
from ipywidgets import widgets, HBox, VBox, Layout
from IPython.display import display

X = +1
O = -1
EMPTY_SPACE = 0

INTERFACE_MAPPING = {
    X: 'X',
    O: 'O'
}

class Interface:
    def __init__(self):
        self.buttons = [
            [
                widgets.Button(
                    description='',
                    layout=Layout(width='100px', height='100px')
                )
                for _ in range(3)
            ]
            for _ in range(3)
        ]

        self.board_widget = VBox([HBox(row) for row in self.buttons])

        self.__player = X
        self.link_positions()

    def on_select_position(self, pos: tuple, button: widgets.Button):
        """Callback on user click on a position of the board

        :param pos: row, column of button on grid
        :param button: clicked button
        """
        if not button.description:
            button.description = INTERFACE_MAPPING.get(self.__player, '')
            self.__player *= -1  # invert player

    def link_positions(self):
        """Link clicks on buttons"""
        for i, row in enumerate(self.buttons):
            for j, button in enumerate(row):
                button.on_click(partial(self.on_select_position, (i, j)))

    def disable_buttons(self):
        """Disable buttons to avoid clicks after end game"""
        for row in self.buttons:
            for button in row:
                button.disabled = True


    def start(self):
        """Display board interface"""
        display(self.board_widget)

interface = Interface()
interface.start()

board = np.zeros((3, 3), dtype=int)
board[:, 1] = O
np.diag(board)
board

def get_game_status(board: np.ndarray) -> Tuple[bool, Union[int, None]]:
    """Check if game ended and who is the winner

    :param board:
    :return: if its a game over, who is the winner
    """
    # check if there is 3 of the same symbol in ...
    finishing_sum = [3 * X, 3 * O]
    for row in board:
        if sum(row) in finishing_sum:
            return True, sum(row) // 3

    for col in board.T:
        if sum(col) in finishing_sum:
            return True, sum(col) // 3

    if sum(np.diag(board)) in finishing_sum:
        return True, sum(np.diag(board)) // 3

    if sum(np.diag(board[:, ::-1])) in finishing_sum:
        return True, sum(np.diag(board)) // 3

    return np.all(board != EMPTY_SPACE), None

def get_possible_moves(board: np.ndarray, player: int = X) -> List[np.ndarray]:
    """Get next possible moves by some player
    """

    possible_moves = []
    for i in range(3):
      for j in range(3):
        if board[i,j] == EMPTY_SPACE: # Corrected comparison
          new_board = board.copy()
          new_board[i, j] = player
          possible_moves.append(new_board)
    return possible_moves

AI_PLAYER = X
HUMAN_PLAYER = O
MAX_N_MOVES = 9


def get_score(winner: int, n_moves: int) -> int:
    """Get how well was the game for the AI:
        - win faster is better than win slower
        - lose slower is better than win faster
        - draw is a intermediary result
    """

    if winner == AI_PLAYER:
        return 10 - n_moves
    elif winner == HUMAN_PLAYER:
        return n_moves -10
    else: return 0

def mini_max(board, player=AI_PLAYER, n_moves=0):
    # Check if it is a maximization or minimization step (who is the player?)
    # Get game status and if it over
    # if game over return the score and board
    # othewise, for each possible move call mini_max and get the score and board
    # choose the action to maximize the score if it is a maximization step
    # otherwise, choose the action to minimize the score
    # return the choosed action and it score

    is_over, winner = get_game_status(board)
    if is_over:
        return get_score(winner, n_moves), board

    possible_boards = get_possible_moves(board, player)
    scores_and_boards = []

    for new_board in possible_boards:
        score, _ = mini_max(new_board, -player, n_moves + 1)
        scores_and_boards.append((score, new_board))

    if player == AI_PLAYER:
        best_move =  max(scores_and_boards, key=lambda x: x[0])
    else:
        best_move =  min(scores_and_boards, key=lambda x: x[0])

    return best_move

board = np.zeros(shape=(3, 3), dtype=np.int8)
_, new_board = mini_max(board, AI_PLAYER)
new_board

new_board = new_board.copy()
new_board[1, 0] = -1
_, new_board = mini_max(new_board, AI_PLAYER)
new_board

END_GAME_MESSAGES = {
    AI_PLAYER: 'AI won!',
    HUMAN_PLAYER: 'You won!',
    EMPTY_SPACE: "It is a draw"
}


class TicTacToeAI(Interface):
    def __init__(self, ai_starts=False):
        super().__init__()
        self.board = np.zeros(shape=(3, 3), dtype=np.int8)
        if ai_starts:
            self.board = min_max(self.board, AI_PLAYER)[1].copy()
            self.update()


    def on_select_position(self, pos: tuple, button: widgets.Button):
        """Callback on user click on a position of the board
        It calls minmax algorithm after each user move

        :param pos: row, column of button on grid
        :param button: clicked button"""
        if not button.description:
            self.board[pos] = HUMAN_PLAYER
            self.board = mini_max(self.board, AI_PLAYER)[1].copy()

            is_over, winner = get_game_status(self.board)
            if is_over:
                self.disable_buttons()
                print(END_GAME_MESSAGES.get(winner))

            self.update()

    def update(self):
        """Update interface from virtual board"""
        for i, row in enumerate(self.board):
            for j, item in enumerate(row):
                self.buttons[i][j].description = INTERFACE_MAPPING.get(item, '')

game = TicTacToeAI(ai_starts=False)
game.start()