#!/usr/bin/python3
from helper_functions import readfile, aprint

# Day 8: Handheld Halting -- AOC 2020

def run_instruction(instructions, run_instructions=[], accumulator=0, i=0):
    '''Run boot code instructions until an instruction repeat'''
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
    elif instruction == 'jmp':
        i += instruction_value
    else:
        i += 1

    return run_instruction(instructions, run_instructions=run_instructions, 
        accumulator=accumulator, i=i)

def fix_instruction(instructions, run_instructions=[], accumulator=0, i=0):
    '''Run altered boot code instructions until end of program reached'''
    
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
    elif instruction == 'jmp':
        i += instruction_value
    else:
        i += 1
    
    return fix_instruction(instructions, run_instructions=run_instructions, 
            accumulator=accumulator, i=i)

if __name__ == '__main__':
    instructions = readfile('inputs/day8.txt', split=None)
    
    aprint(1, run_instruction(instructions))

    # Brute force solve the corruption
    for ind, c in enumerate(instructions):
        # Make a single change of jmp -> nop 
        if 'jmp' in c:
            instructions[ind] = c.replace('jmp', 'nop')
            if fix_instruction(instructions, run_instructions=[], accumulator=0, i=0):
                aprint(2, fix_instruction(instructions, run_instructions=[], accumulator=0, i=0))
                break
            else:
                # Revert change for next iteration
                instructions[ind] = c.replace('nop', 'jmp')
        
        # Make a single change of nop -> jmp
        elif 'nop' in c:
            instructions[ind] = c.replace('nop', 'jmp')
            if fix_instruction(instructions, run_instructions=[], accumulator=0, i=0):
                aprint(2, fix_instruction(instructions, run_instructions=[], accumulator=0, i=0))
                break
            else:
                # Revert change for next iteration
                instructions[ind] = c.replace('jmp', 'nop')