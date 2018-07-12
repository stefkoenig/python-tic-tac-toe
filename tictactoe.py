def define_players():
  player1 = input('Player 1, you will begin. Would you like to play as X or O? ').upper()

  while player1 != 'X' and player1 != 'O':
    player1 = input('Please choose X or O ').upper()
  if player1 == 'X':
    player2 = 'O'
  else:
    player2 = 'X'

  players = dict()
  players['player1'] = player1
  players['player2'] = player2
  players['activePlayer'] = player1

  print('player1 you are: ', player1)
  print('player2 you are: ', player2)

  return players

def print_board(board):
  print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
  print('------------------')
  print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
  print('------------------')
  print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )

def take_turn(board, players, winner):
  activePlayer = players['activePlayer']
  print("It's your turn, ", activePlayer)
  userInput = int(input('Choose where you want to go '))
  while board[userInput] != ' ':
    userInput = int(input('Please choose an empty tile '))
  else:
    board[userInput] = activePlayer
    print_board(board)
    winner = check_for_winner(board, players, winner)
    if activePlayer == players['player1']:
      players['activePlayer'] = players['player2']
    else:
      players['activePlayer'] = players['player1']


  gameState = dict()
  gameState['board'] = board
  gameState['players'] = players
  gameState['winner'] = winner

  return gameState

def check_for_winner(board, players, winner):
  activePlayer = players['activePlayer']

  if ((board[1] == activePlayer and board[2] == activePlayer and board[3] == activePlayer) or
  (board[4] == activePlayer and board[5] == activePlayer and board[6] == activePlayer) or
  (board[7] == activePlayer and board[8] == activePlayer and board[9] == activePlayer) or 
  (board[1] == activePlayer and board[5] == activePlayer and board[9] == activePlayer) or
  (board[7] == activePlayer and board[5] == activePlayer and board[3] == activePlayer) or
  (board[7] == activePlayer and board[4] == activePlayer and board[1] == activePlayer) or
  (board[8] == activePlayer and board[5] == activePlayer and board[2] == activePlayer) or
  (board[9] == activePlayer and board[6] == activePlayer and board[3] == activePlayer)):
    print(activePlayer + ' you win!')
    winner = True
  elif all([board[x] != ' ' for x in range(1,10)]):
    print('No winner!')
    winner = 'tie'
  else:
    winner = False
  return winner

def setup_game():
  winner = False
  board = [' '] * 10
  print('Hello! Welcome to Tic Tac Toe')
  players = define_players()
  print_board(board)
  play_game(board, players, winner)

def play_game(board, players, winner):
  while winner == False:
   gameState = take_turn(board, players, winner)
   winner = gameState['winner']
  else:
    restartGame = input('Would you like to play again? Y or N? ').upper()
    if restartGame == 'Y':
      setup_game()
    else:
      print('Thanks for playing!')


setup_game()