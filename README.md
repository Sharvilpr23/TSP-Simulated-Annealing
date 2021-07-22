# TSP-Simulated-Annealing
This program attempts at solving the travelling salesman problem using simulated annealing algorithm.\
# Travelling Salesman Problem
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city.\
This is a classic graph problem modelled as an uindirected weighted graph, such that cities are the graph's vertices, paths are the graph's edges, and a path's distance is the edge's weight. Once we have a complete graph, we attempt to find a Hamiltonian circuit.\
\
So What makes this solution different?\
We use the ideas of simulated annealing and generate an approach inspired by this. So what is simulated annealing?\
# Simulated Annealing
First proposed by KirkPatrick in 1982, and inspired by the annealing proess of physical systems. Annealing corresponds to subjecting a material to a process of heating and slow cooling in order to toughen and reduce brittleness (De Castro).\
#The general algorithm to simulate the algorithm is:
1. Initialize Temperature, Maximum Interations and the Cooling Rate (Alpha).
2. Generate a random number of 'n' cities.

![Working](https://github.com/Sharvilpr23/TSP-Simulated-Annealing/blob/main/media/tsp.gif)

# References
“Hill Climbing and Simulated Annealing.” FUNDAMENTALS OF NATURAL COMPUTING: Basic Concepts,Algorithms, and Applications, by DE CASTRO LEANDRO NUNES, CRC PRESS, 2023. 
