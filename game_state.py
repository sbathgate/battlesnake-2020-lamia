import numpy as np

def get_game_state(game_state):
        # Create the base state matrix, include a border that is one deep
        board = np.zeros([game_state['board']['width']+2, game_state['board']['height']+2])

        # Set the border cell values to -1
        board = board - 1
        board[1:1+game_state['board']['width'], 1:1+game_state['board']['height']] = 0
        
        # Add the snakes
        for snake in game_state['board']['snakes']:
            head_position = True
            for coord in snake['body']:
                if board[coord['y']+1, coord['x']+1] == 0:
                    board[coord['y']+1, coord['x']+1] = 5 if head_position else 1
                    head_position = False
        
        return board

        '''
    TODO: BFS from every snake head, two step.
        3 directions = 1.0 -> weight directions from this. 
        Up, Down available -> 0.5 each
        stage 2: weight available moves by entereance weight:

        [1.0, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0]
        [1.0, 5.0, 0.3, 0.1, 0.0, 0.0, 0.0, 0.0]
        [0.1, 0.3, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0]
        [0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        [0.0, 0.0, 0.0, 0.3, 0.0, 0.0, 0.0, 0.0]
        [0.0, 0.0, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0]
        [0.0, 0.3, 0.5, 5.0, 1.0, 0.0, 0.0, 0.0]
        '''