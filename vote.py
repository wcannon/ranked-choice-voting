#!/usr/bin/env python
'''This class represents a user vote in a 
   ranked multi-choice election where
   one candidate will be elected'''


class Vote(object):

  def __init__(self, choice_list):
    self.choices = choice_list
    self.current = 0
  
  def choice(self):
    '''Return the candidate choice of a vote'''
    
    try:
      candidate = self.choices[self.current]
    except Exception:
      candidate = None
    return candidate

  def move_to_next_choice(self):
    '''Move our pointer to our next choice as a candidate'''
    self.current = self.current + 1
    return 


if __name__ == "__main__":
  vote_list_1 = [2,3,4]
  vote1 = Vote(vote_list_1)
  print vote1.choice()
  print vote1.choices
  print vote1.current
