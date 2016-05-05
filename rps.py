from random import randint
from time import sleep
OPTIONS = ["R", "P", "S"]
LOSE = "You lost!"
WIN = "You won!"
TIE = "It's a tie!"

def decide_winner(user_choice, computer_choice):
  print "You selected %s" % user_choice
  print "Your opponent selected %s" % computer_choice
  user_choice_index = OPTIONS.index(user_choice)
  computer_choice_index = OPTIONS.index(computer_choice)
  if user_choice == computer_choice:
      print TIE
  elif user_choice_index == 0 and computer_choice_index == 2:
      print WIN
  elif user_choice_index == 1 and computer_choice_index == 0:
      print WIN
  elif user_choice_index == 2 and computer_choice_index == 1:
  		print WIN
  elif user_choice_index > 2:
      print "Error! Please select R for Rock, P for Paper, and S for Scissors"
      return
  else:
    	print LOSE     
def play_RPS():
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = OPTIONS[randint(0,len(OPTIONS)-1)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
