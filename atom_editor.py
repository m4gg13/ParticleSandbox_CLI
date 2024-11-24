import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import simulation
import atomproblem

window = tk.Tk()
window.geometry("700x1000")

width = 3
for i in range(width+1):
    window.grid_columnconfigure(i, weight=1, uniform="foo")

# MARK: - helpers

# MARK: - rows
# angular momentum, magnetization
atom_row = 2
type_row = atom_row + 1
basis_row = atom_row + 1
charge_row = basis_row + 1
spin_row = charge_row + 1
particle_row = spin_row + 1
energy_row = particle_row + 1
particle_no_row = energy_row + 1
angular_momentum_row = particle_no_row + 1
magnetization_row = angular_momentum_row + 1
action_button_row = magnetization_row + 1
state_chooser_row = action_button_row + 1
console_row = state_chooser_row + 1

tk.Label(window, text="----ATOM----").grid(row = atom_row, column = 0)

st1 = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)

st1.grid(row = 1, columnspan= width, padx=50, pady=20)
initial_state_file = open("initial_state.json", "r")
st1_text = initial_state_file.read()
st1.insert(tk.END, st1_text)

# MARK: Variable Configuration section
tk.Label(window, text="INITIAL").grid(row = type_row, column = 0)
tk.Label(window, text="->").grid(row = type_row, column = 1)
tk.Label(window, text="FINAL").grid(row = type_row, column = 2)

# tk.Label(window, text="BASIS").grid(row = basis_row, column = 0)
# b1 = tk.Entry(window, width = 20)
# b1.grid(row = basis_row, column = 1)
# basis_file = open("basis.txt", "r")
# b1_text = basis_file.read()
# b1.insert(tk.END, b1_text)
# b2 = tk.Entry(window)
# b2.grid(row = basis_row, column = 2)

tk.Label(window, text="CHARGE").grid(row = charge_row, column = 0)
c1 = tk.Entry(window, width = 20)
c1.grid(row = charge_row, column = 1)
# c2 = tk.Entry(window)
# c2.grid(row = charge_row, column = 2)

tk.Label(window, text="SPIN").grid(row = spin_row, column = 0)
s1 = tk.Entry(window, width = 20)
s1.grid(row = spin_row, column = 1)
# s2 = tk.Entry(window)
# s2.grid(row = spin_row, column = 2)

tk.Label(window, text="ENERGY").grid(row = energy_row, column = 0)
e1 = tk.Entry(window, width = 20)
e1.grid(row = energy_row, column = 1)
e1.insert(0, "0")
e1.config(state="disabled")
e2 = tk.Entry(window)
e2.grid(row = energy_row, column = 2)
e2.config(state="disabled")

tk.Label(window, text="PARTICLE #").grid(row = particle_no_row, column = 0)
p1 = tk.Entry(window, width = 20)
p1.grid(row = particle_no_row, column = 1)
p1.config(state="disabled")
p2 = tk.Entry(window)
p2.grid(row = particle_no_row, column = 2)
p2.config(state="disabled")

tk.Label(window, text="ANGULAR MOMENTUM").grid(row = angular_momentum_row, column = 0)
am1 = tk.Entry(window, width = 20)
am1.grid(row = angular_momentum_row, column = 1)
am1.config(state="disabled")
am2 = tk.Entry(window)
am2.grid(row = angular_momentum_row, column = 2)
am2.config(state="disabled")

tk.Label(window, text="MAGNETIZATION").grid(row = magnetization_row, column = 0)
mz1 = tk.Entry(window, width = 20)
mz1.grid(row = magnetization_row, column = 1)
mz1.config(state="disabled")
mz2 = tk.Entry(window)
mz2.grid(row = magnetization_row, column = 2)
mz2.config(state="disabled")

console = tk.scrolledtext.ScrolledText(window, wrap=tk.WORD)

def print_to_entries(input):
    # c2.delete(0, tk.END)
    # s2.delete(0, tk.END)
    e2.delete(0, tk.END)
    p2.delete(0, tk.END)
    am2.delete(0, tk.END)
    mz2.delete(0, tk.END)
    print("to entries input")
    print(vars(input))
    print(vars(input.properties))
    properties = input.properties
    # print("properties.AngularMomentum")
    # print(properties.AngularMomentum)
    atomproblem.print_problem_details(input)
    # s2.insert(0, result.final_spin)
    e2.config(state="normal")
    e2.insert(0, input.reference_energy)
    e2.config(state="disabled")
    p2.config(state="normal")
    p2.insert(0, input.properties.particle_number.num_spatial_orbitals)
    p2.config(state="disabled")
    print("input.properties.particle_number.num_spatial_orbitals")
    print(input.properties.particle_number.num_spatial_orbitals)
    # print("vars(input.properties.angular_momentum.num_spatial_orbitals)")
    # print(vars(input.properties.angular_momentum.num_spatial_orbitals))
    am2.config(state="normal")
    am2.insert(0, input.properties.angular_momentum.num_spatial_orbitals)
    am2.config(state="disabled")
    # print("vars(input.properties.magnetization.num_spatial_orbitals)")
    # print(vars(input.properties.magnetization.num_spatial_orbitals))
    mz2.config(state="normal")
    mz2.insert(0, input.properties.magnetization.num_spatial_orbitals)
    mz2.config(state="disabled")

def print_to_initial_entries(problem):
    #.delete(0, tk.END)
    # .config(state="normal")
    # .insert(0, problem.properties.particle_number.num_spatial_orbitals)
    # .config(state="disabled")
    p1.delete(0, tk.END)
    p1.config(state="normal")
    p1.insert(0, problem.properties.particle_number.num_spatial_orbitals)
    p1.config(state="disabled")
    am1.delete(0, tk.END)
    am1.config(state="normal")
    am1.insert(0, problem.properties.particle_number.num_spatial_orbitals)
    am1.config(state="disabled")
    mz1.delete(0, tk.END)
    mz1.config(state="normal")
    mz1.insert(0, problem.properties.particle_number.num_spatial_orbitals)
    mz1.config(state="disabled")

def print_to_console(evolution_state):
    str = atomproblem.evolution_to_string(evolution_state)
    console.insert(tk.END, str)
    console.insert(tk.END, '\n')
    
def print_string_to_console(str):
    console.insert(tk.END, str)
    console.insert(tk.END, '\n')
    
def determine_problem_type(initial_state, charge:int=0, spin:int=0):
    (matter_type, state) = simulation.determine_matter_type(initial_state)
    basis = "sto3g"
    print_all = False
    print_comparison = True
    # now choose the right problem to evolve
    match matter_type:
#        case "particle":
#            final_state_json = particleproblem.evolve(state)
        case "atom":
            print_string_to_console("atom matter_type")
            print_string_to_console(state)
            print_string_to_console(state[0].coordinates.x)
            print_string_to_console(state[0].coordinates.y)
            print_string_to_console(state[0].coordinates.z)
            print_string_to_console(state[1].coordinates.x)
            print_string_to_console(state[1].coordinates.y)
            print_string_to_console(state[1].coordinates.z)
            (problem, final_state_json) = atomproblem.get_json_evolution_result_atom_editor(state, charge, spin)
            print_to_initial_entries(problem)
            print_string_to_console("--PROBLEM--")
            print_string_to_console(problem)
            print_to_entries(problem)
            # result = atomproblem.evolve(problem)
            print_string_to_console("--RESULT--")
            print_string_to_console(final_state_json)
            result = final_state_json
#        case "molecule":
#            final_state_json = moleculeproblem.evolve(state)
    return result

# MARK: Action Button Section
def retrieveInput():
    # state
    st1_input = str(st1.get("1.0", tk.END))
    print_string_to_console(st1_input)
    # initial_state_file = open("initial_state.txt", "w")
    # initial_state_file.write(st1_input)
    # basis - TODO fix this! its broken at the moment
    # b1_input = str(b1.get().split('g')[1])
    # b2_input = b2.get()
    # charge
    c1_input = int(c1.get())
    # c2_input = c2.get()
    # spin
    s1_input = int(s1.get())
    # energy - TODO get this to be used again
    # e1_input = e1.get()
    # e2_input = e2.get()
    # # particle # - TODO get this to be used again
    # p1_input = p1.get()
    # p2_input = p2.get()
    evolution_state = determine_problem_type(st1_input, int(c1_input), int(s1_input))
    # print_to_console(evolution_state)
    print("evolution_state")
    print(evolution_state)

tk.Button(window, text='RUN', command = retrieveInput).grid(row=action_button_row, column=0)

# TODO - these buttons need assocaited commands
tk.Button(window, text='RESET').grid(row=action_button_row, column=1)
tk.Button(window, text='QUIT').grid(row=action_button_row, column=2)

console.grid(row=console_row, columnspan=width, padx=60, pady=20)

window.mainloop()

