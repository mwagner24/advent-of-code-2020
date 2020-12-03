#!/usr/bin/python3
from helper_functions import readfile, aprint


# Day 3: Toboggan Trajectory -- AOC 2020


def move_from_slope(coords, x, y):
	width = len(coords[0])
	height = len(coords)
	slope_coords = [(x * i, y * i ) for i in range(height+1)]
	
	trees_encountered = 0
	for c in slope_coords:
		curr_x, curr_y = c

		# Adjust x values for repeating pattern to the right
		if curr_x >= width:
			curr_x = curr_x % width

		if curr_y >= height:
			return trees_encountered

		elif coords[curr_y][curr_x] == '#':
			trees_encountered += 1

	return trees_encountered



if __name__ == '__main__':

	coords = readfile('inputs/day3.txt')

	aprint(1, move_from_slope(coords, 3, 1))

	trees = []
	mult_trees = 1
	for c in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
		num_trees = move_from_slope(coords, c[0], c[1])
		trees.append(num_trees)
		mult_trees *= num_trees

	aprint(2, mult_trees)