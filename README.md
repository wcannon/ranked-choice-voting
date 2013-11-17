ranked-choice-voting
====================

A sample implementation of ranked choice voting - inspired by Minneapolis MN Code of Ordinances  (http://library.municode.com/HTML/11490/level3/COOR_TIT8.5EL_CH167MUELRUCO.html#COOR_TIT8.5EL_CH167MUELRUCO_167.10AP)

To run a sample election:
./election.py

To run an election with your own input file:
./election.py my-election-votes.csv
* Note: I am expecting that an election votes file consists of one "vote" per line where a vote consists of a series of one or more ranked choice elections

Valid ranked choice elections samples
bob,susie,john
bob
susie,fred

This software comes with no warranties or guarantee on results.  Use it at your own risk.  And, by using it you release me from any legal ramifications whatsoever.  And also, enjoy!
