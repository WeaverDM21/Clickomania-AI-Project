Authors: Dylan Weaver, Gavin White
Project: Clickomania AI Project

How to Run:
Execute the script using python main.py or clicking the play button in VS Code

Configuration: Modify these constants in main.py:
BOARD_SIZE → Change board size.
TOTAL_TESTS → Change number of test runs.
TIMEOUT → Change solver timeout.
VERBOSITY → Change verbosity

Terminal Output: 
Prints the board being solved for each test as well as the solution as a list of coordinates 
corresponding to the place to click.

Prints Average IDA* time 
Average IDS time
Average IDA* nodes
Average IDS nodes
Average IDA* memory
Average IDS memory
Percent same answe

.txt output
Prints the depth, the move, and the board at each step

Special notes:
Any boards over 6x6 take incredibly long to run, hence why we added a timeout