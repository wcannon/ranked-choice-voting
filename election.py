#!/usr/bin/env python
'''This class represents a user vote in a ranked multi-choice election where
   one candidate will be elected
Author: William Cannon
Purpose: Inspire quicker voting tabulations.
License: GPLv3'''

import sys
from vote import Vote
import vote_loader 

class Election(object):

  def __init__(self, vote_list):
    self.votes = vote_list
    self.results_dict = {}   # e.g. {candidate-x:100, candidate-y:150....}
    self.total_votes = len(vote_list)
    self.round = 1  # keeping track of number of voting rounds performed
    self.print_intro()

  def get_number_of_candidates(self):
    '''Determine the number of candidates with votes > 0'''
    counter = 0
    candidate_list = []
    for candidate,votes in self.results_dict.items(): 
      if votes > 0:
        counter = counter + 1
        candidate_list.append(candidate)
    return candidate_list,counter

  def print_intro(self):
    print
    print "====================================================="
    print "================= ELECTION RESULTS =================="
    print "====================================================="
    print
    return

  def run_election(self):
    self.tally_votes()
    print
    print "Votes in round %s" % self.round
    self.round = self.round + 1
    self.print_round_status()
    print
    candidate_list,number_of_candidates = self.get_number_of_candidates()

    if number_of_candidates == 1:
      print "Only one candidate in this election."
      self.declare_winner(candidate_list[0])
    elif number_of_candidates == 2: 
      winner =  self.select_winner(candidate_list)
      if winner:
        self.declare_winner(winner)
      else:
        self.declare_tie()
    else:
      winner = self.candidate_with_50_plus_percent()
      if winner:
        self.declare_winner(winner)
      else:
        self.perform_round()
        self.run_election()  
    return

  def select_winner(self, candidate_list):
    '''Assumption: there are two candidates with votes != 0'''
    winner = None
    #print "Candidate finalists: %s" % candidate_list
    candidate_1 = self.results_dict[candidate_list[0]] 
    #print "candidate 1: %s" % candidate_1
    candidate_2 = self.results_dict[candidate_list[1]]
    #print "candidate 2: %s" % candidate_2
    if candidate_1 == candidate_2:
      print "We have a tie!"
    elif candidate_1 > candidate_2:
      print "The election has a winner!"
      print "Winner: %s, Votes: %s" % (candidate_list[0], candidate_1)
      winner = candidate_list[0]
    else: 
      print "The election has a winner!"
      print "Winner: %s, Votes: %s" % (candidate_list[1], candidate_2)
      winner = candidate_list[1]

    return winner

  def candidate_with_50_plus_percent(self):
    '''Determine if there is a candidate with 50% + 1 vote of all votes'''
    # If there is, return the candidate
    total_votes = len(self.votes)
    winning_number = (total_votes / 2) + 1
    for candidate,vote_count in self.results_dict.items():
      if vote_count >= winning_number:
        return candidate
    return None

  def declare_winner(self, candidate):
    '''print the winner and all other candidates and votes at this time'''
    print "\nThe winner of this election is candidate: %s" % candidate
    print "\nTally of votes in final round:"
    for candidate,votes in sorted(self.results_dict.items()):
      print "Candidate: %s, Votes: %s" % (candidate, votes)
    print
    return
 
  def declare_tie(self):
    '''print all candidates and votes at this time'''
    print "There was not a winner of this election.  There is a tie"
    print "Tally of votes in final round:"
    for candidate,votes in sorted(self.results_dict.items()):
      print "Candidate: %s, Votes: %s" % (candidate, votes)
    return
 
  def tally_votes(self):
    '''tally_votes'''
    # first we clear the old results
    self.results_dict = {}

    for vote in self.votes:
      # get the choice, add it to the value in dict if present, or add the key and value of 1 if not
      choice = vote.choice()
      if choice:
        if choice in self.results_dict:
          self.results_dict[choice] = self.results_dict[choice] + 1
        else:
          self.results_dict[choice] = 1
    return

  def print_round_status(self):
    for candidate,votes in sorted(self.results_dict.items()):
      print "Candidate: %s  Votes: %s" % (candidate,votes)
    return


  def get_minimum_votes_candidates(self, specific_vote_count):
    #print "vote_count given is %s" % specific_vote_count
    losers = {}
    for candidate,vote_count in self.results_dict.items():
      if vote_count == specific_vote_count:
        losers[candidate] = vote_count
    #print "losers with minimum votes = %s" % losers
    return losers

  def ask_election_official(self, candidates_in_last):
    print "We have a tie for last place between the following candidates:"
    for key, value in candidates_in_last.items():
      print key
    print "\nYou must choose a candidate from the output above for their votes to be redistributed"
    loser =  raw_input("Please type your choice:")
    return loser

  def redistribute_votes_of_candidate(self, candidate_to_remove):
    for vote in self.votes:
      vote.remove_candidate(candidate_to_remove)
      print vote.choices
    return
 
  def perform_round(self):
    '''Select the candidate with least number of votes.  Redistribute their votes to the other candidates.
       In the event of a tie vote between two candidates, user input is used to decide which one loses
       its votes'''

    ''' Generally:  pick the losing candidate for this round.  Walk through vote list updating
        choice pointer of each vote by incrementing it - e.g.  vote.move_to_next_choice()'''
    votes_list = self.results_dict.values() 
    minimum = min(votes_list) # determine the smallest number of votes allocated to a candidate 
    loser_count = votes_list.count(minimum)  # number of candidates with smallest number of votes e.g. a tie
    if loser_count > 1: # there is a tie for last place with 2+ candidates 
      print "There is a tie between candidates to be eliminated."
      print "An election official must determine which candidate will be removed"
      candidates_in_last = self.get_minimum_votes_candidates(minimum)
      print "Candidates in last: %s" % candidates_in_last.keys()
      candidate_to_remove = self.ask_election_official(candidates_in_last)
    else:
      candidates_in_last = self.get_minimum_votes_candidates(minimum)
      print "Candidate in last: %s" % candidates_in_last
      mycandidate = candidates_in_last.keys()[0]
      candidate_to_remove = mycandidate
      print "removing candidate: %s" % mycandidate

    self.redistribute_votes_of_candidate(candidate_to_remove)     
    self.tally_votes()
    return


if __name__ == "__main__":
 
  try:
    election_file = sys.argv[1]
  except Exception, e:
    election_file = 'election-1.csv'
  
  try: 
    myvotes = vote_loader.load_votes(election_file)
  except Exception, e:
    print "Unable to open election file"
    print e
    sys.exit(1)
  election2 = Election(myvotes)
  election2.run_election()
