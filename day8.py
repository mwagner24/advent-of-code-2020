#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 8: Handheld Halting -- AOC 2020

def run_boot(instructions, run_instructions=[], accumulator=0, i=0, end=False):
    '''Run boot code instructions'''
    if (i in run_instructions and not end) or (end and i == len(instructions)):
        return accumulator
    elif (i in run_instructions and end) or (instructions[i] in ['jmp 0', 'jmp +0', 'jmp -0']):
        return False
    else:
        run_instructions.append(i)

    instruction_split = instructions[i].split(' ')
    instruction = instruction_split[0]
    instruction_value = int(instruction_split[1])

    if instruction == 'acc':
        accumulator += instruction_value
        i += 1
    elif instruction == 'jmp':
        i += instruction_value
    else:
        i += 1

    return run_boot(instructions, run_instructions=run_instructions, 
        accumulator=accumulator, i=i, end=end)

if __name__ == '__main__':
    instructions = readfile('inputs/day8.txt', split=None)
    
    aprint(1, run_boot(instructions))

    # Brute force solve the corruption
    for ind, c in enumerate(instructions):
        # Make a single change of jmp -> nop 
        if 'jmp' in c:
            instructions[ind] = c.replace('jmp', 'nop')
            if run_boot(instructions, run_instructions=[], accumulator=0, i=0, end=True):
                aprint(2, run_boot(instructions, run_instructions=[], accumulator=0, i=0, end=True))
                break
            else:
                # Revert change for next iteration
                instructions[ind] = c.replace('nop', 'jmp')
        
        # Make a single change of nop -> jmp
        elif 'nop' in c:
            instructions[ind] = c.replace('nop', 'jmp')
            if run_boot(instructions, run_instructions=[], accumulator=0, i=0, end=True):
                aprint(2, run_boot(instructions, run_instructions=[], accumulator=0, i=0, end=True))
                break
            else:
                # Revert change for next iteration
                instructions[ind] = c.replace('jmp', 'nop')