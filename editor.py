import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import simulation
import atomproblem

window = tk.Tk()
window.geometry("800x1000")

width = 3
for i in range(width+1):
    window.grid_columnconfigure(i, weight=1, uniform="foo")

# MARK: - helpers

#def smth_to_json():


# MARK: - UI sections
type_row = 2
atom_row = type_row + 1
basis_row = atom_row + 1
charge_row = basis_row + 1
spin_row = charge_row + 1
particle_row = spin_row + 1
energy_row = particle_row + 1
particle_no_row = energy_row + 1
action_button_row = particle_no_row + 1
state_chooser_row = action_button_row + 1
console_row = state_chooser_row + 1

# MARK: Initial & Final Matter Type section
# dropdown in column 1

# dropdown in column 1

# MARK: State Visualization section
# box where i can drag things around and add a button

# box where i can drag things around and add a button

tk.Label(window, text="STATE").grid(row = 1, column = 0)
# st1 = tk.Entry(window, width = 20)
st1 = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)

# st1.grid(row = state1_row, column = 1)
st1.grid(row = 1, columnspan= width)
initial_state_file = open("initial_state.json", "r")
st1_text = initial_state_file.read()
st1.insert(tk.END, st1_text)
st2 = tk.Entry(window)
# st2.grid(row = state2_row, column = 2)
# st2.grid(row = 1, columnspan = width)

# MARK: Variable Configuration section
tk.Label(window, text="INITIAL").grid(row = type_row, column = 0)
tk.Label(window, text="->").grid(row = type_row, column = 1)
tk.Label(window, text="FINAL").grid(row = type_row, column = 2)

tk.Label(window, text="----ATOM----").grid(row = atom_row, column = 0)

tk.Label(window, text="BASIS").grid(row = basis_row, column = 0)
b1 = tk.Entry(window, width = 20)
b1.grid(row = basis_row, column = 1)
basis_file = open("basis.txt", "r")
b1_text = basis_file.read()
b1.insert(tk.END, b1_text)
b2 = tk.Entry(window)
b2.grid(row = basis_row, column = 2)

tk.Label(window, text="CHARGE").grid(row = charge_row, column = 0)
c1 = tk.Entry(window, width = 20)
c1.grid(row = charge_row, column = 1)
c2 = tk.Entry(window)
c2.grid(row = charge_row, column = 2)

tk.Label(window, text="SPIN").grid(row = spin_row, column = 0)
s1 = tk.Entry(window, width = 20)
s1.grid(row = spin_row, column = 1)
s2 = tk.Entry(window)
s2.grid(row = spin_row, column = 2)

tk.Label(window, text="----PARTICLE?----").grid(row = particle_row, column = 0)

tk.Label(window, text="ENERGY").grid(row = energy_row, column = 0)
e1 = tk.Entry(window, width = 20)
e1.grid(row = energy_row, column = 1)
e2 = tk.Entry(window)
e2.grid(row = energy_row, column = 2)

tk.Label(window, text="PARTICLE #").grid(row = particle_no_row, column = 0)
p1 = tk.Entry(window, width = 20)
p1.grid(row = particle_no_row, column = 1)
p2 = tk.Entry(window)
p2.grid(row = particle_no_row, column = 2)

# MARK: State Chooser dropdown section

# MARK: Console section
console = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)

def print_to_entries(result):
    # initial_state_file = open("initial_state.json", "r")
    # st1_text = initial_state_file.read()
    # disperse result into its constituent fields
    e1_text = result.initial_energy
    e2_text = result.final_energy
    s1_text = result.initial_spin
    s2_text = result.final_spin
    p1_text = result.initial_num_particles
    p2_text = result.final_num_particles
    # clear the fields first
    # st1.delete(0, tk.END)
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    s1.delete(0, tk.END)
    s2.delete(0, tk.END)
    p1.delete(0, tk.END)
    p2.delete(0, tk.END)
    # then fill the fields with the appropriate value (:
    # st1.insert(0, st1_text)
    e1.insert(0, e1_text)
    e2.insert(0, e2_text)
    s1.insert(0, s1_text)
    s2.insert(0, s2_text)
    p1.insert(0, p1_text)
    p2.insert(0, p2_text)

def print_to_console(evolution_state):
    str = atomproblem.evolution_to_string(evolution_state)
    console.insert(tk.END, str)
    console.insert(tk.END, '\n')
    
def print_string_to_console(str):
    console.insert(tk.END, str)
    console.insert(tk.END, '\n')

def runButton():
    evolution_state = determine_problem_type()
    print_to_entries(evolution_state)
    print_to_console(evolution_state)
    
def determine_problem_type(initial_state, basis:str="sto3g", charge:int=0, spin:int=0):
    # TODO: figure out how to get inital state here
    # with open("initial_state.json") as initial_ state:
    #     initial_state = initial_state.read()
    (matter_type, state) = simulation.determine_matter_type(initial_state)
    # temporary values for the things we need
    # basis = "sto3g"
    # charge = 0
    print_all = False
    print_comparison = True
    # now choose the right problem to evolve
    match matter_type:
#        case "particle":
#            final_state_json = particleproblem.evolve(state)
        case "atom":
            print_string_to_console("atom matter_type")
            print_string_to_console(state)
            result = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
#        case "molecule":
#            final_state_json = moleculeproblem.evolve(state)
    return result

# MARK: Action Button Section
#tk.Button(window, text='RUN', command = run_simulation).grid(row=action_button_row, column=1)
# atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
# pretty sure we'll want to use the evolve function here since we're getting
#     in these relevant variables
def retrieveInput():
    # state
    # st1_input = st1.get()
    st1_input = str(st1.get("1.0", tk.END))
    print_string_to_console(st1_input)
    # initial_state_file = open("initial_state.txt", "w")
    # initial_state_file.write(st1_input)
    st2_input = st2.get()
    # basis
    print_string_to_console("--b1.get().split('g')[1]--")
    print_string_to_console(b1.get().split('g')[1] == '\r')
    print_string_to_console('------')
    b1_input = str(b1.get().split('g')[1])
    b2_input = b2.get()
    # charge
    c1_input = int(c1.get())
    c2_input = c2.get()
    # spin
    s1_input = int(s1.get())
    s2_input = s2.get()
    # energy
    e1_input = e1.get()
    e2_input = e2.get()
    # particle #
    p1_input = p1.get()
    p2_input = p2.get()
    # params are state, basis, charge, spin
    evolution_state = determine_problem_type(st1_input, str(b1_input), c1_input, s1_input)
    # evolution_state = determine_problem_type(st1_input, "sto3g", 1, 1)
    print_to_entries(evolution_state)
    print_to_console(evolution_state)

tk.Button(window, text='RUN', command = retrieveInput).grid(row=action_button_row, column=0)
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
