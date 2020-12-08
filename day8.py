#!/usr/bin/python3
from helper_functions import readfile, aprint
import re

# Day 8:  -- AOC 2020

def run_instruction(instructions, run_instructions, accumulator=0, i=0):
    if i in run_instructions:
        return accumulator
    else:
        run_instructions.append(i)

    instruction_split = instructions[i].split(' ')
    instruction = instruction_split[0]
    instruction_value = int(instruction_split[1])

    if instruction == 'acc':
        accumulator += instruction_value
        i += 1
        return run_instruction(instructions, run_instructions, accumulator, i)

    elif instruction == 'jmp':
        i += instruction_value
        return run_instruction(instructions, run_instructions, accumulator, i)

    else:
        i += 1
        return run_instruction(instructions, run_instructions, accumulator, i)


def fix_instruction(instructions, run_instructions, accumulator=0, i=0):
    # Program ends when instruction number == total number of instructions + 1
    if i == len(instructions):
        return accumulator
    # Terminate on single-instruction infinite loops, repeat instructions, or instructions beyond scope
    elif i > len(instructions) or instructions[i] in ['jmp +0', 'jmp 0', 'jmp -0'] or i in run_instructions:
        return False
    else:
        run_instructions.append(i)
    
    instruction_split = instructions[i].split(' ')
    instruction = instruction_split[0]
    instruction_value = int(instruction_split[1])

    if instruction == 'acc':
        accumulator += instruction_value
        i += 1
        return fix_instruction(instructions, run_instructions, accumulator, i)

    elif instruction == 'jmp':
        i += instruction_value
        return fix_instruction(instructions, run_instructions, accumulator, i)

    else:
        i += 1
        return fix_instruction(instructions, run_instructions, accumulator, i)

if __name__ == '__main__':
    instructions = readfile('inputs/day8.txt', split=None)
    
    aprint(1, run_instruction(instructions, [], accumulator=0, i=0))

    # Brute force solve the corruption
    for ind, c in enumerate(instructions):
        if 'jmp' in c:
            # Brute force jmp -> nop replacements
            instructions[ind] = c.replace('jmp', 'nop')
            if fix_instruction(instructions, [], accumulator=0, i=0):
                aprint(2, fix_instruction(instructions, [], accumulator=0, i=0))
                break
            else:
                # Revert change for next iteration
                instructions[ind] = c.replace('nop', 'jmp')