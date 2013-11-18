#!/usr/bin/env python
'''This simply reads in a csv file of votes, and produces a list of votes'''
import csv
from vote import Vote

CSVFILE = 'election-1.csv'

def load_votes(csv_file=CSVFILE):
  '''Read a csv file - each line is a vote, return a list of votes'''
  myvotes = []
  try:
    #with open(csv_file, 'rb') as f:
    with open(csv_file, 'rU') as f:
      reader = csv.reader(f)
      for row in reader:
        newvote = Vote(row)
        myvotes.append(newvote)
  except Exception, e:
    raise
  return myvotes
      

def main():
  all_votes = load_votes()
  return all_votes


if __name__ == "__main__":
  votes_read_in = main()
  for vote in votes_read_in:
    print vote.choice()
