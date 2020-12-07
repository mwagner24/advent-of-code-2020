#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 1: Report Repair -- AOC 2020

def find_two_entries(entries):
	for i in entries:
		for j in entries:
			if int(i) + int(j) == 2020:
				return int(i) * int(j)

def find_three_entries(entries):
	for i in entries:
		for j in entries:
			for k in entries:
				if int(i) + int(j) + int(k) == 2020:
					return int(i) * int(j) * int(k)

if __name__ == '__main__':
	entries = readfile('inputs/day1.txt')
	aprint(1, find_two_entries(entries))
	aprint(2, find_three_entries(entries))