#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 9: Encoding Error -- AOC 2020

def xmas_decoder(encoded, preamble_len=25, find_contiguous=False):
    ''''Decode eXchange-Masking Addition System (XMAS) encryption''' 
    for curr_index, number in enumerate(encoded[preamble_len:]):
        if not validate_number(number, encoded[curr_index:preamble_len+curr_index]):
            if find_contiguous:
                return find_contiguous_range(number, encoded)
            else:
                return number

def validate_number(number, priors):
    '''Ensure at least one pair of numbers within current preamble-based list sum to current number'''
    for i, p in enumerate(priors):
        for j, p2 in enumerate(priors):
            if i != j:
                if p + p2 == number:
                    return True
    return False

def find_contiguous_range(checksum, segment, min_len=2):
    '''Find the contiguous set of at least two numbers in the list'''
    for a in range(len(segment)):
        for z in range(len(segment)):
            if (sum(segment[a:z]) == checksum) and (z+1 - a >= min_len):
                return min(segment[a:z]) + max(segment[a:z])

if __name__ == '__main__':
    encoded = readfile('inputs/day9.txt', split=None)
    encoded = [int(e) for e in encoded]
    aprint(1, xmas_decoder(encoded))
    aprint(2, xmas_decoder(encoded, find_contiguous=True))