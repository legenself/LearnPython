import curses
from random import randrange,choice
from collections import defaultdict

actions=["Up","Left","Down","Right","Restart","Exit"]

letter_codes=[ord(ch) for ch in 'WASDRQwasdrq']

action_dict=dict(zip(letter_code,action*2))

def main(stdscr)

  def init():
      return 'Game'

  def not_game(state)

      responses=defaultdict(lambda:state)

      responses['Restart'],responses['Exit']='Init','Exit'

      return responses[action]

  def game()

     if action=='Restart':
         return 'Init'
     if action=='Exit':
         return 'Exit'
       if 
