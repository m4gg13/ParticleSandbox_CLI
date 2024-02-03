import json
import cmath

# https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/05%3A_Multi-Particle_Systems
#
# https://hbar.uchicago.edu/hbar_exp.php
# h_bar = 1.054571817×10^-34 J-s
#
# x_i - coordinate of particle i
# p_i - momentum of particle i
# m_i - mass of particle i
# t, time - time steps

def run_simulation(modus_operandi, initial_state, time, forward):
        # this is where the fun stuff goes!!!
    #	output = "{ \"the result!\": 1 }"
    #	output_str = json.dumps(output, indent=4)

    H = make_hamiltonian(5, 2, time)

    with open("final_state.json") as final_state:
        final_state = final_state.read()

    return H

def make_hamiltonian(coordinate, mass, time):
    h_bar = 1.054571817 * 10**-34

    x_i = coordinate
    p_i = -1 * i * h_bar * partial_over_partial(x_i)
    m_i = mass

    t = time

    H = (p_i**2 / (2 * m_i)) + potential(x_i, t)

def partial_over_partial(coordinate):
    # not sure yet
    return 1

def potential(coordinate, time):
    # not sure yet
    return 1
