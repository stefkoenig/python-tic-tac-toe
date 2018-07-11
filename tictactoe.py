def define_players():
  player1 = input('Player 1, you will begin. Would you like to play as X or Y? ').upper()
  
  while player1 != 'X' and player1 != 'Y':
    player1 = input('Please choose X or Y ').upper()
  if player1 == 'X':
    player2 = 'Y'
  else:
    player2 = 'X'

  print('player1 you are: ', player1)
  print('player2 you are: ', player2)

def setup_game():
  print('Hello! Welcome to Tic Tac Toe')
  define_players()


setup_game()