#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 6: Custom Customs -- AOC 2020

def get_unique_answers(group):
    '''Return number of unique 'yes' answers for a group'''
    return len(set([l for l in group.replace(' ', '')]))

def get_all_answers_yes(group):
    '''Return count of unanimous "yes" answers within group by member''' 
    group_dict = {}
    members = group.split(' ')
    for member in members:
        for answer in member:
            if answer not in group_dict:
                group_dict[answer] = 1
            else:
                group_dict[answer] += 1
    count_all_yes = 0
    for ans in group_dict:
        if group_dict[ans] == len(members):
            count_all_yes += 1
    return count_all_yes

if __name__ == '__main__':
    with open('inputs/day6.txt', 'r+') as f:
        text = [ t.replace('\n', ' ') for t in str(f.read()).split('\n\n') ] 

        count, count_all_yes = 0, 0
        for group in text:
            count += get_unique_answers(group)
            count_all_yes += get_all_answers_yes(group)

        aprint(1, count)
        aprint(2, count_all_yes)