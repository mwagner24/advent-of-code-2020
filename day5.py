#!/usr/bin/python3
from helper_functions import readfile, aprint

import re

# Day 5: Binary Boarding -- AOC 2020


class BoardingPass(object):
	'''Boarding Pass Object for Binary Space Partitioning'''

	def __init__(self, instructions):
		self.instructions = instructions
		self.row_instructions = instructions[:-3]
		self.seat_instructions = instructions[-3:]

	@staticmethod
	def iter_split(instructions, start_min, start_max, upper='B', lower='F'):
		min_, max_ = start_min, start_max

		for half in instructions:
			if half == upper:
				min_ = int( (max_ + min_) / 2) + 1
			else:
				max_ = int( (max_ + min_) / 2) 

		if instructions[-1] == lower:
			return min_

		return max_

	def get_row(self):
		'''Row-wise Binary Space Partitioning'''
		return self.iter_split(self.row_instructions, 0, 127)


	def get_seat(self):
		'''Column-wise Binary Space Partitioning'''
		return self.iter_split(self.seat_instructions, 0, 7, upper='R', lower='L')

	def get_seat_id(self):
		row = self.get_row()
		seat = self.get_seat()
		return (row * 8) + seat


if __name__ == '__main__':
	boarding_passes = readfile('inputs/day5.txt')
	seat_ids = []
	for p in boarding_passes:
		seat_ids.append(BoardingPass(p).get_seat_id())
	seat_ids = sorted(seat_ids)

	aprint(1, seat_ids[-1])

	seat_ids_lag = seat_ids[1:]
	seat_ids_lag.append(0)
	for seat, seatl in zip(seat_ids, seat_ids_lag):
		if seatl-seat == 2:
			aprint(2, seat+1)