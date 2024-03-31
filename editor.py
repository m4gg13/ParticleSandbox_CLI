import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import simulation
import atomproblem

window = tk.Tk()
window.geometry("800x800")

width = 3
for i in range(width+1):
    window.grid_columnconfigure(i, weight=1, uniform="foo")

# MARK: - helpers

#def smth_to_json():

def determine_problem_type():
    # TODO: figure out how to get inital state here
    with open("initial_state.json") as initial_state:
        initial_state = initial_state.read()
    (matter_type, state) = simulation.determine_matter_type(initial_state)
    # temporary values for the things we need
    basis = "sto3g"
    charge = 0
    spin = 0
    print_all = False
    print_comparison = True
    # now choose the right problem to evolve
    match matter_type:
#        case "particle":
#            final_state_json = particleproblem.evolve(state)
        case "atom":
            result = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
#        case "molecule":
#            final_state_json = moleculeproblem.evolve(state)
    return result


# MARK: - UI sections
type_row = 1
initial_state_row = type_row + 1
final_state_row = initial_state_row + 1
state_row = final_state_row + 1
energy_row = state_row + 1
spin_row = energy_row + 1
particle_number_row = spin_row + 1
action_button_row = particle_number_row + 1
state_chooser_row = action_button_row + 1
console_row = state_chooser_row + 1

# MARK: Initial & Final Matter Type section
# dropdown in column 1
tk.Label(window, text="->").grid(row = type_row, column = 1)
# dropdown in column 1

# MARK: State Visualization section
# box where i can drag things around and add a button

# box where i can drag things around and add a button

# MARK: Variable Configuration section
tk.Label(window, text="INITIAL").grid(row = state_row, column = 1)
tk.Label(window, text="FINAL").grid(row = state_row, column = 2)

tk.Label(window, text="ENERGY").grid(row = energy_row, column = 0)
# TODO: how to read in from the text box?
e1 = tk.Entry(window, width = 20)
e1.grid(row = energy_row, column = 1)
e2 = tk.Entry(window)
e2.grid(row = energy_row, column = 2)

tk.Label(window, text="SPIN").grid(row = spin_row, column = 0)
s1 = tk.Entry(window, width = 20)
s1.grid(row = spin_row, column = 1)
s2 = tk.Entry(window)
s2.grid(row = spin_row, column = 2)

tk.Label(window, text="PARTICLE #").grid(row = particle_number_row, column = 0)
p1 = tk.Entry(window, width = 20)
p1.grid(row = particle_number_row, column = 1)
p2 = tk.Entry(window)
p2.grid(row = particle_number_row, column = 2)

# MARK: State Chooser dropdown section

# MARK: Console section
console = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)

def print_to_entries(result):
    e1_text = result.initial_energy
    e2_text = result.final_energy
    s1_text = result.initial_spin
    s2_text = result.final_spin
    p1_text = result.initial_num_particles
    p2_text = result.final_num_particles
    e1.insert(0, e1_text)
    e2.insert(0, e2_text)
    s1.insert(0, s1_text)
    s2.insert(0, s2_text)
    p1.insert(0, p1_text)
    p2.insert(0, p2_text)

def print_to_console(evolution_state):
    str = atomproblem.evolution_to_string(evolution_state)
    console.insert(tk.END, str)

def runButton():
    evolution_state = determine_problem_type()
    print_to_entries(evolution_state)
    print_to_console(evolution_state)

# MARK: Action Button Section
#tk.Button(window, text='RUN', command = run_simulation).grid(row=action_button_row, column=1)
# atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
# pretty sure we'll want to use the evolve function here since we're getting
#     in these relevant variables
tk.Button(window, text='RUN', command = runButton).grid(row=action_button_row, column=0)
tk.Button(window, text='RESET').grid(row=action_button_row, column=1)
tk.Button(window, text='QUIT').grid(row=action_button_row, column=2)

console.grid(row=console_row, columnspan=width)

window.mainloop()

# MARK: - notes
#from tkinter import *
#from tkinter import messagebox
#top = Tk()
#top.geometry("100x100")
#def helloCallBack():
#   msg=messagebox.showinfo( "Hello Python", "Hello World")
#B = Button(top, text ="Hello", command = helloCallBack)
#B.place(x=50,y=50)
#top.mainloop()
