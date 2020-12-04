#!/usr/bin/python3
from helper_functions import readfile, aprint

import re

# Day 4: Passport Processing -- AOC 2020


def read_passports_to_dict(file):
	'''Parse input and return dict of each passport's metadata'''
	with open(file, 'r+') as f:
		text = f.read()		

	text = text.split('\n\n')
	text = [t.replace('\n',' ').split(' ') for t in text]

	passports = {}
	for i, entry in enumerate(text):
		passports[i] = {}
		for kv in entry:
			kvsplit = kv.split(':')
			passports[i][kvsplit[0]] = kvsplit[1]

	return passports

def validate_fields(passports):
	'''Confirm that required passport fields are present'''
	valid = []
	req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

	for k in passports:
		valid_count = 0
		for req in req_fields:
			if req in passports[k]:
				valid_count += 1
		if valid_count == 7:
			valid.append(passports[k])
	return valid

def validate_between(field, min_, max_):
	'''Validator function to confirm a number is between two numbers'''
	return int(field) >= min_ and int(field) <= max_

def validate_height(hgt):
	'''Validate height units and min/max'''
	if 'cm' == hgt[-2:]:
		height = re.findall(r'(\d+)\s*cm', hgt)
		if not height:
			return False
		return validate_between(height[0], 150, 193)

	elif 'in' == hgt[-2:]:
		height = re.findall(r'(\d+)\s*in', hgt)
		if not height:
			return False
		return validate_between(height[0], 59, 76)

	else:
		return False

def validate_hair_color(hcl):
	'''Validate Hair Color format'''
	if len(hcl) != 7 or hcl[0] != '#':
		return False
	else:
		for char in hcl[1:]:
			if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
			'a', 'b', 'c', 'd', 'e', 'f']:
				return False
		return True

def validate_eye_color(ecl):
	'''Validate Eye Color abbreviation'''
	return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(pid):
	'''Validate nine-digit Passport ID with leading zeroes'''
	if len(pid) != 9:
		return False
	else:
		for p in pid:
			if p not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
				return False
	return True

def strict_validate_passports(passports):
	'''Validate each field's values'''
	passports = validate_fields(passports)

	strict_valid = []
	for passport in passports:
		validator = []
		validator.append(validate_pid(passport['pid']))
		validator.append(validate_eye_color(passport['ecl']))
		validator.append(validate_hair_color(passport['hcl']))
		validator.append(validate_height(passport['hgt']))
		validator.append(validate_between(passport['eyr'], 2020, 2030))
		validator.append(validate_between(passport['iyr'], 2010, 2020))
		validator.append(validate_between(passport['byr'], 1920, 2002))
		if sum(validator) == 7:
			strict_valid.append(passport)

	return strict_valid


if __name__ == '__main__':
	passports = read_passports_to_dict('inputs/day4.txt')
	aprint(1, len(validate_fields(passports)))
	aprint(1, len(strict_validate_passports(passports)))