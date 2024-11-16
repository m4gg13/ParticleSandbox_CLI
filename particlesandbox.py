# global
import sys
import os
import subprocess
import json
import re

# local
from simulation import *
import particle

# print about each of the input types
def modus_operandi():
    print("|-----Modus Operandi-----|\n")
    global modus_operandi

    while True:
        with open("config.json") as config:
            print(config.read())

        response = input("Is this the modus operandi you'd like to use?\n\nPlease say 'Yes' or 'No'\n>")

        if handle_yn_response(response, "config.json") != "neither":
            # if they answered "neither" they need to try again
            break

        with open("config.json") as config:
            modus_operandi = config.read()
    print("\n|------------------------|\n\n")
    return modus_operandi

def initial_state():
    print("|-------Initial State-------|\n")
    global initial_state

    while True:
        with open("initial_state.json") as initial_state:
            print(initial_state.read())
        response = input("Is this the initial state you'd like to use?\n\nPlease say 'Yes' or 'No'\n>")
        if handle_yn_response(response, "initial_state.json") != "neither":
                        # if they answered "neither" they need to try again
            with open("initial_state.json") as initial_state:
                initial_state = initial_state.read()
            error = validate_state_syntax(initial_state)
            if not error:
                break
            else:
                print(f'Invalid state: {error}')
    print("\n|------------------------|\n\n")
    return initial_state

def steps():
    print("|----------Steps----------|\n")
    global steps
    while True:
        steps = input("How many steps in time would you like to take?\n>")
        error = validate_steps(steps)
        if not error:
            break
        else:
            print(f'Invalid number or steps: {error}')
    print("\n|------------------------|\n\n")
    return steps

def direction():
    print("|--------Direction--------|\n")
    global forward
    while True:
        direction = input("Would you like to move forward or backward in time?\n>")

        d = direction.lower()
        if d == "forward" or d == "f" or d == ">":
            forward = True
            break
        elif d == "backward" or d == "b" or d == "<":
            forward = False
            break
        else:
            print("Please say 'Forward' or 'Backward'")
    print("\n|------------------------|\n\n")
    return forward

def print_final_state(final_state):
    print("\n|-------Final State-------|\n")
    print(final_state)
    print("\n|------------------------|\n\n")

# validate and handle various kinds of input to prevent hax!!!
def validate_state_syntax(state):
	with open("schema.json") as schema:
		schema = schema.read()
    # TODO
	# check things with schema and type(), implement later
	return ""

def validate_steps(steps):
	# TODO
	return ""

def handle_yn_response(response, filename):
	r = response.lower()
	if r == "yes" or r == "y":
		return "yes"
	elif r == "no" or r == "n":
		print("Well shoot. Changing it at this point isn't implemented\n")
		# open the file, have then write to it then save and close it
		return "no"
	else:
		print("Please say 'Yes' or 'No'\n")
		return "neither"

# the one that prints everything
def wizard():
    print("*+>~.. PARTICLE SANDBOX ..~<+*\n\n")
    # get the initial state
    i = initial_state()
#    particles = translate_initial_state_to_particles(i)
    # and print out whats going on there
#    for p in particles:
#        print(str(p.number))
    final_state = run_simulation(1, i, 1, 1)
    # get the final state
#    final_state = translate_particles_to_final_state(particles)
    # and print out whats going in in there!
    print_final_state(final_state)
    print("\n")
    print("*+>~.. *+>~.......~<+* ..~<+*\n\n")

# main
wizard()


