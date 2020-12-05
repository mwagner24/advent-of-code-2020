#!/usr/bin/python3

def readfile(file):
	'''Reads generic line-based AOC input'''
	with open(file, 'r') as f:
		return [ a.rstrip() for a in f.readlines() ]

def aprint(answer, *args):
	'''Prints answers in standard format'''
	print(f'Answer {answer}:', *args)