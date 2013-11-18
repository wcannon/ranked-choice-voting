#!/usr/bin/env python
"""
Usage:
  election_votes_generator.py OUTPUT_FILE VOTERS CANDIDATES ALLOWED_CHOICES

Generate a simulated result set of an election - a csv file of votes, 1 per line

Arguments:
  OUTPUT_FILE		Name of output file to put simulated election results into
  VOTERS   		Number of voters voting in the election
  CANDIDATES    	Number of candidates that a vote can choose from 
  ALLOWED_CHOICES  	Number of choices allowed in the rank voting (e.g. 3 choices)
 
Options:
  -h --help

"""
import csv
from docopt import docopt
import random


def create_simulated_election(num_votes, candidates_total, allowed_choices_per_vote):
  number_of_votes = int(num_votes)
  number_of_candidates = int(candidates_total)
  number_of_choices_per_vote = int(allowed_choices_per_vote)

  election = []  # append all votes (as a list) to this list

  for i in xrange(number_of_votes):
    choices = []
    for c in xrange(number_of_choices_per_vote):
      candidate_choice = random.randint(1, number_of_candidates)
      choices.append(candidate_choice) 
    #print "Vote: %s" % choices
    election.append(choices)
  return election

def write_out_election_results(output_file, election):
  f = open(output_file, 'w')
  for vote in election:
    line = []
    for choice in vote:
      line.append(str(choice))
    line = ",".join(line) + "\n"
    f.write(line)
  f.close()
  return


if __name__ == "__main__":
  arguments = docopt(__doc__)
  #print "arguments: %s" % arguments
  results = create_simulated_election(arguments['VOTERS'], arguments['CANDIDATES'], arguments['ALLOWED_CHOICES'])
  write_out_election_results(arguments['OUTPUT_FILE'], results)
  print "all done" 
