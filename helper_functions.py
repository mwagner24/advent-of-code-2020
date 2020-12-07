#!/usr/bin/python3

def readfile(file, split=None):
	'''Reads generic line-based AOC input'''
	with open(file, 'r') as f:
		if not split:
			return [ a.rstrip() for a in f.readlines() ]
		else:
			return str(f.read()).split(split)

def aprint(answer, *args):
	'''Prints answers in standard format'''
	print(f'Answer {answer}:', *args)