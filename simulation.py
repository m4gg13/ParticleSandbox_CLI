# global... kinda. not really
import json
import cmath
import sympy as sp
import numpy as np

from qiskit.circuit import ParameterVector
from qiskit.quantum_info import SparsePauliOp
from qiskit.quantum_info import Statevector
from qiskit_algorithms import TimeEvolutionProblem
from qiskit_algorithms import TrotterQRTE

#local
import matter
import particle
import atom
import molecule

import particleproblem
import atomproblem
import moleculeproblem

# MARK: logistical things

# this is the old one that doesnt respond to which type of matter we're dealing with
def run_simulation_dumb(modus_operandi, initial_state, time, forward):
    # use the initial state to determine what particles to include
    print("read in initial state\n")
#    with open("initial_state.json") as initial_state_file:
#        print(initial_state_file.read())
#        initial_state = initial_state_file.read()
    initial_particles = translate_initial_state_to_particles(initial_state)
    print("get the composite hamiltonian of the initial particles\n")
    composite_hamiltonian = 0
    for particle in initial_particles:
        # use the energies to make the hamiltonian
        hamiltonian = make_sparse_pauli_op(particle, time)
        # add the hamiltonian for that particle to the composite
        composite_hamiltonian += hamiltonian
    # use the composite hamiltonian and the particles to make the time evolution problem
    print("create the time evolution problem\n")
    print(composite_hamiltonian)
    problem = make_time_evolution_problem(composite_hamiltonian, initial_particles, time)
    # use trotterization to solve the problem
    print("evolve the problem")
    trotter = TrotterQRTE()
    result = trotter.evolve(problem)
    evolved_state = Statevector(result.evolved_state)
    # dictionary of probabilities
    amplitudes_dict = evolved_state.probabilities_dict()
    print("amplitudes_dict\n")
    print(amplitudes_dict)
    # turn the result into an array of particles
    final_particles = make_result_into_particles(result)
    # and the set of particles into json!
#    final_state = translate_particles_to_final_state(final_particles)
    # write the result to the `final_state.json` file
    with open("final_state.json") as final_state:
        final_state = final_state.read()
    return final_state

def run_simulation(modus_operandi, initial_state, time, forward):
    # use the initial state to determine what type of matter
    (matter_type, state) = determine_matter_type(initial_state)
    # based on the matter type, choose which model to use for hamiltonian
    match matter_type:
#        case "particle":
#            final_state_json = particleproblem.evolve(state)
        case "atom":
            final_state_json = atomproblem.get_json_evolution_result(state)
#        case "molecule":
#            final_state_json = moleculeproblem.evolve(state)
    # make the json object into a string
    final_state_str = json.dumps(final_state_json)
    # write out the final state to the appropriate file
    final_state_file = open("final_state.json", "w")
    final_state_file.write(final_state_str)
    final_state_file.close()
    return final_state_str

def count_qubits_required():
    # TODO
    return 2

# right now this isn't smart about determining matter type
# there's got to be a more solid way of doing that
# maybe throw an error if there are conflicting matter types
# in the initial state?
def determine_matter_type(initial_state):
    # make `initial_state` string into json object
    initial_state_dictionary = json.loads(initial_state)
    # need to peek at each piece of the json object
    keys = list(initial_state_dictionary.keys())
    # collect all of the pieces of the json object here
    # in their particle sandbox form
    matter = []
    for key in keys:
        match key:
            case "particle":
                p = particle.Particle(1)
                matter.append(p)
                matter_type = p.type
            case "up":
                up = particle.UpQuark(1)
                matter.append(up)
                matter_type = up.type
            case "down":
                down = particle.DownQuark(1)
                matter.append(down)
                matter_type = down.type
            case "proton":
                proton = particle.Proton(1)
                matter.append(proton)
                matter_type = proton.type
            case "hydrogen":
                for h in initial_state_dictionary["hydrogen"]:
                    hydrogen = atom.Hydrogen(1)
                    # really should probably check to see whether the object has these
                    # keys before just boldly using them
                    hydrogen.coordinates.x = h["x"]
                    hydrogen.coordinates.y = h["y"]
                    hydrogen.coordinates.z = h["z"]
                    matter.append(hydrogen)
                matter_type = hydrogen.type
    return_tuple = (matter_type, matter)
    return return_tuple

def translate_initial_state_to_particles(initial_state):
    print(initial_state)
    initial_state_dictionary = json.loads(initial_state)
    keys = list(initial_state_dictionary.keys())
    particles = []
    for key in keys:
        match key:
            case "up":
                up = particle.UpQuark(1)
                particles.append(up)
            case "down":
                down = particle.DownQuark(1)
                particles.append(down)
            case "proton":
                proton = particle.Proton(1)
    return particles

def translate_particles_to_final_state(particles):
    final_state_dictionary = {}
    for p in particles:
        key = p.name
        if key in final_state_dictionary.keys():
            count = final_state_dictionary[key]
            final_state_dictionary[key] = count + 1
        else:
            final_state_dictionary[key] = 1
    final_state = json.dumps(final_state_dictionary)
    return final_state

# MARK: algorithm things

def make_time_evolution_problem(hamiltonian, particles, time):
    final_time = time
    initial_state = translate_particles_to_statevector(particles)
    print("initial state vector\n")
    print(initial_state)
    problem = TimeEvolutionProblem(hamiltonian, initial_state=initial_state, time=final_time)
    return problem

def make_result_into_particles(result):
    # check out the evolved state in circuit form
    circuit = result.evolved_state
    circuit.draw('mpl')
    print(circuit)
    # can make the circuit into a statevector
    statevector = Statevector(circuit)
    # and the statevector into a set of particles!
    final_particles = translate_statevector_to_particles(statevector)
    return final_particles

def translate_particles_to_statevector(particles):
    # REVIEW
    # somehow translate the particles into a spin string
    # gonna figure out what's right experimentally for this part
    #
    # First spin up, second spin down
    # Note: the labels are interpreted from right to left!
    count = len(particles)
    spins = ""
    for i in range(count):
        spins = spins + "0"
    return Statevector.from_label(spins)

def translate_statevector_to_particles(statevector):
    # TODO
    # somehow translate the statevector into a set of particles
    print("statevector:")
    print(statevector)
    particle1 = particle
    particle2 = particle
    return [particle1, particle2]

# MARK: energy things

# the tutorial calls the return value of this fn the hamiltonian
def make_sparse_pauli_op(particle, time):
    coordinate = particle.coordinate
    mass = particle.mass
    kinetic = get_kinetic_energy(particle, time) # ("ZX", [n_i], 1)
    potential = get_potential_energy(particle, time) # ("Y", [n_i], 1)
    count = count_qubits_required()
    # example: SparsePauliOp.from_sparse_list([("ZX", [1, 4], 1), ("YY", [0, 3], 2)], num_qubits=5)
    op = SparsePauliOp.from_sparse_list([kinetic, potential], num_qubits=count)
    return op.simplify()

def get_kinetic_energy(particle, time):
    # the param `particle` holds things like the particle's
    # number, mass and momentum... and coordinate(?)
    h_bar = 1.054571817 * 10**-34
    i = cmath.sqrt(-1)
    n_i = particle.number
    x_i = particle.coordinate
    p_i = -1 * i * h_bar * partial_over_partial(x_i)
    m_i = particle.mass
    t = time
    kinetic = (p_i**2 / (2 * m_i))
    # P_i = p_i**2
    # M_i = 1 / (2 * m_i)
    # TODO
    # formatted_kinetic = ("PM", [n_i, n_i], 1)
    formatted_kinetic = ("ZX", [n_i], 1)
    #  + get_potential_energy(x_i, t)
    # needs to return something of the form
    # ("<symbols>", [index of each of the symbols respectively], number to multiply the whole expression by)
    return formatted_kinetic

def get_potential_energy(particle, time):
    # TODO
    n_i = particle.number
    x_i = particle.coordinate
    # needs to return something of the form
    # ("<symbols>", [index of each of the symbols respectively], number to multiply the whole expression by)
    formatted_potential = ("Y", [n_i], 1)
    return formatted_potential

# MARK: math things
def partial_over_partial(coordinate):
    # TODO
    return 1

# MARK: main
#number = 1
#mass = 2
#coordinate = 3
#particle = particle.Particle(number, mass, coordinate)
#print(particle.mass)
#print(get_kinetic_energy(particle, 2))
#initial_state = "{ [ \"proton\": 1 ] }"
#particles = translate_initial_state_to_particles(initial_state)
#for p in particles:
#    print(p.number)

# MARK: notes
# ----------------------------- https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/05%3A_Multi-Particle_Systems
#
# https://hbar.uchicago.edu/hbar_exp.php
# h_bar = 1.054571817×10^-34 J-s
#
# x_i - coordinate of particle i
# p_i - momentum of particle i
# m_i - mass of particle i
# t, time - time steps, float or double or something
