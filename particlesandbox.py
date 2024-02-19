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

# scrub

# this isn't used. maybe someday
# basically just add escapes to any double quotes within the string
def scrub_initial_state(initial_state):
    # first, remove newlines
    initial_state = initial_state.replace("\n", "")
    scrubbed_initial_state = initial_state.strip()
    # then find the first index of a double quote
    double_quote_index = initial_state.find('"')
    # a -1 means that there aren't any more double quotes in the given string
    while double_quote_index != -1:
        # place an escape character right before the double quote and put the string back together
        start = scrubbed_initial_state[:double_quote_index]
        end = scrubbed_initial_state[double_quote_index:]
        scrubbed_initial_state = start + "\\" + end
        # now we want to find the next double quote so lets look just beyond where we found the previous
        start_next_double_quote_index = double_quote_index + 4
        # don't want to walk off the end of the string though
        if start_next_double_quote_index > len(scrubbed_initial_state):
            break
        # like we said we'll only look at the end of the string
        # and if we find one we'll use it for the next iteration otherwise it'll be -1
        double_quote_index = scrubbed_initial_state.find('"', start_next_double_quote_index)
    return scrubbed_initial_state

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


