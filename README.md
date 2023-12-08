# Python_exam

Step 1: Code a serial Python version of the game of life

You can implement Conway's game of life using numpy array or cupy array to hold data. Neighbours are defined as adjacent cells.

Any LIVING cell with 2 or 3 neighbours survives.
Any DEAD cell with 3 neighbours comes alive.
Any OTHER LIVING cell dies.
All deaths and births occur simultaneously
So, at each step you need:

calculate the number of neighnours
set "dead" or "alive" status according to the above
plot
Hints and directions

For initial conditions you can start from one of the two files "ships.txt" and "gun.txt", that are provided n this Github repo (but feel free to create your own if you wish). You can read them like

field=np.genfromtxt("ships.txt").transpose()
Step 2.A: Parallelize the code with MPI4Py, using the same approach adopted in the Jacobi exercise seen in the course by Ivan

*You can distribute the "big" matrix by rows among the MPI tasks.

Step 2.B: Write a test to compare the final configuration obtained by the parallel version with the one of serial version

Step 3: Choose one of the following frameworks (Numba-parallel, Multiprocessing, Joblib) to parallelize the operations inside each MPI task

Note: For parallel versions you are only required to print the final configuration of the game, after a chosen number of steps.
