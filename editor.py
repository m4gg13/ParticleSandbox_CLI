import tkinter as tk

import simulation

window = tk.Tk()
window.geometry("800x800")

# MARK: Initial & Final Matter Type section
type_row = 1
# dropdown in column 1
tk.Label(window, text="->").grid(row = type_row, column = 2)
# dropdown in column 1

# MARK: State Visualization section
initial_state_row = type_row + 1
# box where i can drag things around and add a button

final_state_row = initial_state_row + 1
# box where i can drag things around and add a button

# MARK: Variable Configuration section
state_row = final_state_row + 1
tk.Label(window, text="INITIAL").grid(row = state_row, column = 2)
tk.Label(window, text="FINAL").grid(row = state_row, column = 3)

energy_row = state_row + 1
tk.Label(window, text="ENERGY").grid(row = energy_row, column = 1)
# TODO: how to read in from the text box?
e1 = tk.Entry(window, width = 20)
e1.grid(row = energy_row, column = 2)
e2 = tk.Entry(window)
e2.grid(row = energy_row, column = 3)

spin_row = energy_row + 1
tk.Label(window, text="SPIN").grid(row = spin_row, column = 1)
s1 = tk.Entry(window, width = 20)
s1.grid(row = spin_row, column = 2)
s2 = tk.Entry(window)
s2.grid(row = spin_row, column = 3)

particle_number_row = spin_row + 1
tk.Label(window, text="PARTICLE #").grid(row = particle_number_row, column = 1)
p1 = tk.Entry(window, width = 20)
p1.grid(row = particle_number_row, column = 2)
p2 = tk.Entry(window)
p2.grid(row = particle_number_row, column = 3)

# MARK: Action Button Section
action_button_row = particle_number_row + 1
#tk.Button(window, text='RUN', command = run_simulation).grid(row=action_button_row, column=1)
# atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
# pretty sure we'll want to use the evolve function here since we're getting
#     in these relevant variables
tk.Button(window, text='RUN', command = determine_problem_type).grid(row=action_button_row, column=1)
tk.Button(window, text='RESET').grid(row=action_button_row, column=2)
tk.Button(window, text='QUIT').grid(row=action_button_row, column=3)

# MARK: State Chooser dropdown section
state_chooser_row = action_button_row + 1

# MARK: Console section
console_row = state_chooser_row + 1

window.mainloop()

# MARK: - helpers

#def smth_to_json():

def determine_problem_type():
    # figure out how to get inital state here
    (matter_type, state) = determine_matter_type(initial_state)
    match matter_type:
#    case "particle":
#        final_state_json = particleproblem.evolve(state)
    case "atom":
        final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
#    case "molecule":
#        final_state_json = moleculeproblem.evolve(state)

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
