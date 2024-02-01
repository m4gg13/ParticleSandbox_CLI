# global
import sys
import os
import subprocess
import json

# local
from simulation import run_simulation

def wizard():
	print("*+>~.. PARTICLE SANDBOX ..~<+*\n\n")

	print("----Modus Operandi----\n")
	global modus_operandi
	get_modus_operandi_msg_1()
	while True:
		response = input("Is this the modus operandi you'd like to use?\n\nPlease say 'Yes' or 'No'\n>")

		if handle_yn_response(response) != "neither":
			# if they answered "neither" they need to try again		
			break

	# should be able to take a file or a string
	while True:
		# keep my url in user_config.json?
		# print("Opening initial_state.json")
		
		# state = input("What would you like to use as your initial state? /Users/maggiezirnhelt/private/ParticleSandbox_CLI/initial_state.json\r")

		#state = input("What would you like to use as your initial state?\n\n")		

		print("----Initial State----\n")

		state = "/Users/maggiezirnhelt/private/ParticleSandbox_CLI/initial_state.json"
		with open(state) as initial_state:
			print(initial_state.read())

		response = input("Is this the initial state you'd like to use?\n\nPlease say 'Yes' or 'No'\n>")

		error = validate_state_syntax(state)

		if not error:
			break
		else:
			print(f'Invalid state: {error}')

	while True:
		global steps
		steps = input("How many steps in time would you like to take?\n")
		error = validate_steps(steps)

		if not error:
			break
		else:
			print(f'Invalid number or steps: {error}')			 

	while True:
		direction = input("Would you like to move forward or backward in time?\n")
	
		global forward	
		if direction.lower() == "forward":
			forward = True 
			return
		elif direction.lower() == "backward":
			forward = False
			return
		else:
			print("Please say 'Forward' or 'Backward'")

def get_modus_operandi_msg_1():
	with open("config.json") as config:
    		print(config.read())


def get_modus_operandi_msg():
	question = "Is this the modus operandi you'd like to use?\n\n"
	status, modus_operandi = subprocess.getstatusoutput(f'cat config.json\n\n')
	#modus_operandi = "[2 up + 1 down = 1 proton,\n 1 up + 2 down = 1 neutron]\n\n"
	return question + ' ' + modus_operandi

def validate_state_syntax(state):
	# this feels dangerous but i can't tell why...
	os.system(f'sudo open {state}')
	# os.system(f'sudo /System/Applications/TextEdit.app/Contents/MacOS/TextEdit {state}')
	
	while True:
		done = input("When you've saved and closed your state file, please say 'Done'\n\n")

		if done.lower() == "done":
			break
		else:
        		print("If you're done you gotta say 'Done'")	

	global initial_state
	status, initial_state = subprocess.getstatusoutput(f'cat {state}\\n\n')

	status, schema = subprocess.getstatusoutput('cat schema.json\n\n')

	# check things with schema and type(), implement later

	return ""

def validate_steps(steps):
	# this isnt implemented yet
	return ""

def handle_yn_response(response):
	if response.lower() == "yes":
                return "yes"
        elif response.lower() == "no":
                print("Well shoot. Changing it at this point isn't implemented\n")
                # open the file, have then write to it then save and close it
                return "no"
        else:
                print("Please say 'Yes' or 'No'\n")
		return "neither"

wizard()
run_simulation(modus_operandi, initial_state, steps, forward)
