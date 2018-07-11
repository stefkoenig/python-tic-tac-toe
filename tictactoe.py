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

def print_board():
  board = [{"7": ""},{8: ""},{9: ""}, {4: ""},{5: ""},{6: ""}, {1: ""},{2:""},{3:""}]
  print("----------------")
  for i in board:
    boardValue = list(i.values())
    print(boardValue[0])
    # print("|", j, "|", end = " ")
    print()
    print("----------------")


def setup_game():
  print('Hello! Welcome to Tic Tac Toe')
  players = define_players()
  print_board()
  activePlayer = players['activePlayer']
  print(activePlayer)


setup_game()