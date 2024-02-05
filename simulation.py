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
import particle

# logistical things
def run_simulation(modus_operandi, initial_state, time, forward):
    # use the initial state to determine what particles to include
    # ... and where?
    initial_particles = translate_initial_state_to_particles(initial_state)
    composite_hamiltonian = 0
    for particle in initial_particles:
        # use the energies to make the hamiltonian
        hamiltonian = make_sparse_pauli_op(particle, time)
        # add the hamiltonian for that particle to the composite
        composite_hamiltonian += hamiltonian
    # use the composite hamiltonian and the particles to make the time evolution problem
    problem = make_time_evolution_problem(composite_hamiltonian, particles, time)
    # use trotterization to solve the problem
    trotter = TrotterQRTE()
    result = trotter.evolve(problem)
    # check out the evolved state in circuit form
    circuit = result.evolved_state
    circuit.draw('mpl')
    # can make the circuit into a statevector
    statevector = Statevector(circuit)
    # and the statevector into a set of particles!
    final_particles = translate_statevector_to_particles(statevector)
    # and the set of particles into json!s
    final_state = translate_particles_to_final_state(final_particles)
    # write the result to the `final_state.json` file
    with open("final_state.json") as final_state:
        final_state = final_state.read()
    # return something?
    return circuit

def count_qubits_required():
    # TODO
    return 2

def translate_initial_state_to_particles(initial_state):
    # TODO
    number = 1
    mass = 2
    coordinate = 3
    # .Particle(number, mass, coordinate)
    particle1 = particle
    # .Particle(number, mass, coordinate)
    particle2 = particle
    return [particle1, particle2]

def translate_particles_to_final_state(particles):
    # TODO
    final_state = "{ [ \"up\": 2, \"down\": 1 ] }"
    return final_state

# algorithm things

def make_time_evolution_problem(hamiltonian, particles, time):
    final_time = time
    initial_state = translate_particles_to_statevector(particles)
    problem = TimeEvolutionProblem(hamiltonian, initial_state=initial_state, time=final_time)
    return problem

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

def translate_particles_to_statevector(particles):
    # TODO
    # somehow translate the particles into a spin string
    #
    # First spin up, second spin down
    # Note: the labels are interpreted from right to left!
    return Statevector.from_label('10')

def translate_statevector_to_particles(statevector):
    # TODO
    # somehow translate the statevector into a set of particles
    particle1 = particle
    particle2 = particle
    return [particle1, particle2]

# energy things
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

# math things
def partial_over_partial(coordinate):
    # TODO
    return 1

# main
number = 1
mass = 2
coordinate = 3
particle = particle.Particle(number, mass, coordinate)
print(get_kinetic_energy(particle, 2))

# notes
# ----------------------------- https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/05%3A_Multi-Particle_Systems
#
# https://hbar.uchicago.edu/hbar_exp.php
# h_bar = 1.054571817×10^-34 J-s
#
# x_i - coordinate of particle i
# p_i - momentum of particle i
# m_i - mass of particle i
# t, time - time steps, float or double or something
