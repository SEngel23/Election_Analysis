# Election_Analysis
---
## Project Overview
1. Calculate the total number of votes.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
---
## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.9.12, Visual Studio Code 1.71.2
---
## Summary
The analysis of the election show that: 
- There were 369,711 votes case in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
    - Diana Degette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

Code Output
File Resource: [election_analysis.txt](Resources/election_results.csv)
```
Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
------------------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------------------
```

---
## Challenge Overview


---
## Challenge Summary



``` python
import os
import pandas as pd 

```
