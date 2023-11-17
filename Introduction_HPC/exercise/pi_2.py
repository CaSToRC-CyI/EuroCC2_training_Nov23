"""
Perform a Monte Carlo simulation to calculate pi
Numpy version
"""
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--n", help="Number of iterations",
                    type=int)
args = parser.parse_args()

# Populate two numpy arrays with n random numbers in the 0-1 range
x, y = np.random.random(args.n), np.random.random(args.n)
# Now calculate the distances from the origin
distances = np.sqrt(x**2+y**2)
# Sum the number of points that lie below distance=1
dist_sum = np.sum(np.where(distances < 1, 1, 0))
# Finally calculate pi
pi = 4*(dist_sum/args.n)
print(f"pi = {pi}")