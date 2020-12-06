from itertools import zip_longest, count
from operator import mul
from functools import reduce

def product(iterable):
	return reduce(mul, iterable, 1)

class Grid:
	def __init__(self, grid):
		self.grid = grid
		self.xmax = len(grid[0])
		self.ymax = len(grid)

	def __getitem__(self, coordinates):
		x, y = coordinates
		return self.grid[y][x % self.xmax]

	def pos_range(self, start=(0,0), step=(1, 1)):
		x0, y0 = start
		dx, dy = step
		return zip(count(x0, dx), range(y0, self.ymax, dy))

with open('3.in') as f:
	grid = Grid([line.strip() for line in f])

OPEN, TREE = '.#'

slope = (3, 1)
part1 = sum(grid[x, y] == TREE for x, y in grid.pos_range(step=slope))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
part2 = product(
	sum(grid[x, y] == TREE for x, y in grid.pos_range(step=slope))
	for slope in slopes
)

print('Part 1:', part1)
print('Part 2:', part2)