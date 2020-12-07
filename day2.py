#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 2: Password Philosophy -- AOC 2020

class OTCP(object):
	'''Validates a password under Official Toboggan Corporate Policy'''

	def __init__(self, pass_string, delim=' ', policy_delim='-'):
		self.pass_split = pass_string.split(delim)
		self.policy_first = int(self.pass_split[0].split(policy_delim)[0])
		self.policy_second = int(self.pass_split[0].split(policy_delim)[1])
		self.alpha_instance = self.pass_split[1][0]
		self._password = self.pass_split[-1]

	def _validate_password(self):
		'''Validates a password under the new OTCP policy'''
		counter = 0
		for char in self._password:
			if char == self.alpha_instance:
				counter +=1

		return counter >= self.policy_first and counter <= self.policy_second

	def validate_password(self):
		'''Validates a password under the current OTCP policy'''
		checks = 0
		for i in [self.policy_first - 1, self.policy_second -1]:
			if self._password[i] == self.alpha_instance:
				checks += 1

		return checks == 1

	@classmethod
	def _count_valid_from_file(cls, file):
		'''Returns the number of valid passwords under old policy'''
		pass_policies = readfile(file)
		c = 0
		for p in pass_policies:
			if cls(p)._validate_password():
				c += 1
		return c

	@classmethod
	def count_valid_from_file(cls, file):
		'''Returns the number of valid passwords under current policy'''
		pass_policies = readfile(file)
		c = 0
		for p in pass_policies:
			if cls(p).validate_password():
				c += 1
		return c

if __name__ == '__main__':
	aprint(1, OTCP._count_valid_from_file('inputs/day2.txt'))
	aprint(2, OTCP.count_valid_from_file('inputs/day2.txt'))