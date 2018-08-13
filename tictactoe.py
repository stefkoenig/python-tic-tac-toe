import random

def choose_first_player(players):
  coin_toss = random.randint(0,1)
  
  if coin_toss == 0:
    return 'X'
  else:
    return 'O'
  
def define_players():
  player1 = ''
  while player1 != 'X' and player1 != 'O':
    player1 = input('Player 1, please choose X or O ').upper()
  if player1 == 'X':
    player2 = 'O'
  else:
    player2 = 'X'

  players = dict()
  players['player1'] = player1
  players['player2'] = player2

  print('player1 you are: ', player1)
  print('player2 you are: ', player2)

  players['active_player'] = choose_first_player(players)

  return players

def print_board(board):
  print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] )
  print('------------------')
  print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] )
  print('------------------')
  print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] )

def take_turn(board, players, winner):
  active_player = players['active_player']
  print("It's your turn, ", active_player)
  user_input = int(input('Choose where you want to go '))
  while user_input > 9 or user_input < 1 or board[user_input] != ' ':
    user_input = int(input('Please choose an empty tile '))
  else:
    board[user_input] = active_player
    print_board(board)
    winner = check_for_winner(board, players, winner)
    if active_player == players['player1']:
      players['active_player'] = players['player2']
    else:
      players['active_player'] = players['player1']

  game_state = dict()
  game_state['board'] = board
  game_state['players'] = players
  game_state['winner'] = winner

  return game_state

def check_for_winner(board, players, winner):
  active_player = players['active_player']

  if ((board[1] == active_player and board[2] == active_player and board[3] == active_player) or
  (board[4] == active_player and board[5] == active_player and board[6] == active_player) or
  (board[7] == active_player and board[8] == active_player and board[9] == active_player) or
  (board[1] == active_player and board[5] == active_player and board[9] == active_player) or
  (board[7] == active_player and board[5] == active_player and board[3] == active_player) or
  (board[7] == active_player and board[4] == active_player and board[1] == active_player) or
  (board[8] == active_player and board[5] == active_player and board[2] == active_player) or
  (board[9] == active_player and board[6] == active_player and board[3] == active_player)):
    print(active_player + ' you win!')
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
   game_state = take_turn(board, players, winner)
   winner = game_state['winner']
  else:
    restart_game = input('Would you like to play again? Y or N? ').upper()
    if restart_game == 'Y':
      setup_game()
    else:
      print('Thanks for playing!')


setup_game()
