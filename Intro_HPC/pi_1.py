"""
Perform a Monte Carlo simulation to calculate pi
"""
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="Number of iterations",
                    type=int)
args = parser.parse_args()

# Generate two vectors of n random numbers in the 0-1 range
# First create two empty lists
x = []
y = []

# Populate them
for i in range(args.n):
    x.append(random.random())
    y.append(random.random())

# Create a new list to note the points which are a maximum of
# 1 unit away from the origin (0, 0)
distances = []
for i in range(args.n):
    if (x[i]**2 + y[i]**2)**0.5 < 1:
        distances.append(1)
    else:
        distances.append(0)

# Sum up the ones in the distances list
dist_sum = 0
for i in range(args.n):
    dist_sum += distances[i]
    
# Finally calculate pi
pi = 4*(dist_sum/args.n)
print(f"pi = {pi}")
