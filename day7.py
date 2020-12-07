#!/usr/bin/python3
from helper_functions import readfile, aprint
import re

# Day 7: Handy Haversacks -- AOC 2020

def parse_rule(rule):
    '''Regex lines of file input to return key, value pairs of bag colors and their components'''
    key = re.findall(r'([a-z ]+) bags contain', rule)[0]
    values = re.findall(r'(\d+) ([a-z ]+) bag', rule)
    return key, [v[1] for v in values for a in range(int(v[0]))]

def get_children(bag, bags_dict, contains):
    '''Recursively step through each bag color to find if child exists'''
    if contains in bags_dict[bag]:
        return True
    else:
        for bc in set(bags_dict[bag]):
            if get_children(bc, bags_dict, contains):
                return True

def get_n_bags(bag, bags_dict, bag_of_bags=[], debug=True):
    '''Recursively step through a bag color to find number of nested bags'''
    if debug:
        print(f'Working on bag: {bag}')
    bag_of_bags.append(len(bags_dict[bag]))
    for ibag in bags_dict[bag]:
        if bags_dict[ibag]:
            get_n_bags(ibag, bags_dict, bag_of_bags=bag_of_bags, debug=debug)
    return sum(bag_of_bags)

if __name__ == '__main__':
    DEBUG = False
    text = readfile('inputs/day7.txt')
    
    # Create dict: key: bag color,  value: list of bags the bag color contains
    bags = {}
    for rule in text:
        k,v = parse_rule(rule)
        bags[k] = v

    count = 0
    for bag in bags:
        if DEBUG:
            print(f'Current count: {count}, checking bag: {bag}')
        if get_children(bag, bags, 'shiny gold'):
            count += 1
    aprint(1, count)

    aprint(2, get_n_bags('shiny gold', bags, debug=DEBUG))