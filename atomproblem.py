from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_nature.second_q.mappers import JordanWignerMapper

import json

# TODO: find a way to determine and report what the final state
#   of the system is in terms of type like `matter`, `particle`, `atom`, `molecule`
#   since for ex H_2 atomic input state ends up being a molecule output state
def evolve(state, basis:str="sto3g", charge:int=0, spin:int=0, print_all:bool=False, print_comparison:bool=False):
    # make atom - looks like this `"H 0 0 0; H 0 0 0.735"`
    atoms = translate_state_to_atoms(state)
    final_stateobj = AtomProblemState("initial", state, atoms, basis, charge, spin, print_all, print_comparison)
    # determine the problem
    driver = PySCFDriver(
        atom=atoms,
        basis=basis,
        charge=charge,
        spin=spin,
        unit=DistanceUnit.ANGSTROM,
    )
    problem = driver.run()
    hamiltonian = problem.hamiltonian
#    print_hamiltonian_details(hamiltonian)
    # hamiltonian.nuclear_repulsion_energy  # NOT included in the second_q_op above
#    print_problem_details(problem)
    # now make the solver
    solver = GroundStateEigensolver(
        JordanWignerMapper(),
        NumPyMinimumEigensolver(),
    )
    result = solver.solve(problem)
#    print_result_details(result)
    # round to one decimal since results won't be exact(?)
    initial_energy = round(result.total_energies[0], 1)
    final_energy = round(problem.reference_energy, 1)
    final_atoms = []
    print_energy_details(initial_energy, final_energy)
    if initial_energy == final_energy:
        print("the system is the same as it was at the beginning")
        # we can return the initial state as the final state
        final_atoms = state
    elif initial_energy > final_energy:
        # the energy increased in the evolution, not sure what that would mean actually!
        print("the energy of the system increased in the evolution")
        final_state = state
#    elif initial_energy < final_energy:
#        print("the energy of the system decreased in the evolution")
#        final_state =
    if print_all:
        print_all(hamiltonian, problem, result, initial_energy, final_energy)
    max_problem_energy = find_max_energy(problem)
    if print_comparison:
        print_problem_result(problem, result, max_problem_energy, initial_energy, final_energy, spin)
    final_state = translate_atoms_to_state(final_atoms)
    # TODO: the charge and spin are not accurate here pretty sure
    initial_state = state
    initial_atoms = []
    initial_spin = spin
    final_spin = result.spin
    initial_num_particles = atoms.count(';') + 1
    final_num_particles = result.num_particles
    result = EvolutionSummary(initial_state,
                              final_state,
                              initial_atoms,
                              final_atoms,
                              initial_energy,
                              final_energy,
                              initial_spin,
                              final_spin,
                              initial_num_particles,
                              final_num_particles,
                              hamiltonian,
                              problem,
                              result)
    return result

def get_json_evolution_result(state,
                              basis:str="sto3g",
                              charge:int=0, spin:int=0,
                              print_all:bool=False,
                              print_comparison:bool=False):
    result = evolve(state, basis, charge, spin, print_all, print_comparison)
    final_state = result.final_state
    final_atoms = result.final_atoms
    final_stateobj = AtomProblemState("final",
                                      final_state,
                                      final_atoms,
                                      basis,
                                      charge,
                                      spin,
                                      print_all,
                                      print_comparison)
    return "{\"hydrogen\": 2}"

def determine_candidate_states():
    # 1. gotta figure out which results have the right number of atoms
    # as those are the only ones that could possibly be correct
    # 2. it also only makes sense that the final state energy is smller
    # than that of the initial
    return ""


def translate_state_to_atoms(state):
    i = 0
    final_atoms = ""
    for atom in state:
        # if this isn't the first atom, add a semicolon
        if i > 0:
            final_atoms += "; "
        # figure out what kind of atom we're dealing with
        match atom.name:
            case "hydrogen":
                # make atom - looks like this for example `"H 0 0 0; H 0 0 0.735"`
                coordinates = atom.coordinates.describe()
                final_atoms = final_atoms + "H " + coordinates
        i+=1
    return final_atoms

# returns a json string representing the atom collection
def translate_atoms_to_state(atoms):
    final_state_dictionary = {}
    for atom in atoms:
        key = atom.name
        if key in final_state_dictionary.keys():
            count = final_state_dictionary[key]
            final_state_dictionary[key] = count + 1
        else:
            final_state_dictionary[key] = 1
    final_state = json.dumps(final_state_dictionary)
    return final_state

# (state, basis, charge, spin, print_all, print_comparison)
class AtomProblemState:
    def __init__(self, stage, state, atoms, basis, charge, spin, print_all, print_comparison):
        self.stage = stage
        self.state = state
        self.atoms = atoms
        self.basis = basis
        self.charge = charge
        self.spin = spin
        self.print_all = print_all
        self.print_comparison = print_comparison

# MARK: logging

def find_max_energy(problem):
    # list(problem.second_q_ops()[0].items())[0][1]
#    print("list(problem.second_q_ops()[0].items())[0][1]")
#    print(list(problem.second_q_ops()[0].items())[0][1])
#    print("list(problem.second_q_ops()[0].items())[1][1]")
#    print(list(problem.second_q_ops()[0].items())[1][1])
#    print("list(problem.second_q_ops()[0].items())[2][1]")
#    print(list(problem.second_q_ops()[0].items())[2][1])
#    print("list(problem.second_q_ops()[0].items())[3][1]")
#    print(list(problem.second_q_ops()[0].items())[3][1])
#    print("list(problem.second_q_ops()[0].items())[4][1]")
#    print(list(problem.second_q_ops()[0].items())[4][1])
    #
    i = 0
    max = 0.0
    while i < 36:
#        print("abs(list(problem.second_q_ops()[0].items())[i][1]) > abs(max):")
#        print(abs(list(problem.second_q_ops()[0].items())[i][1]) > abs(max))
#        print("abs(list(problem.second_q_ops()[0].items())[i][1]):")
#        print(abs(list(problem.second_q_ops()[0].items())[i][1]))
#        print("max:")
#        print(max)
        if abs(list(problem.second_q_ops()[0].items())[i][1]) > abs(max):
            max = list(problem.second_q_ops()[0].items())[i][1]
#            print("new max:")
#            print(max)
        i += 1
    print("max energy:")
    print(max)
    return max

def print_hamiltonian_details(hamiltonian):
    print("-----HAMILTONIAN-----")
    print("hamiltonian.electronic_integrals.alpha:")
    coefficients = hamiltonian.electronic_integrals
    print(coefficients.alpha)
    second_q_op = hamiltonian.second_q_op()
    print(second_q_op)
    print("----------")

def hamiltonian_to_string(hamiltonian):
    str = "-----HAMILTONIAN-----\n"
    str = str + "hamiltonian.electronic_integrals.alpha:\n"
#    coefficients = hamiltonian.electronic_integrals
#    str = str + coefficients
#    str = str + "\n"
    str = str + hamiltonian.second_q_op()
    str = str + "\n"
    str = str + "----------\n"
    return str

def print_problem_details(problem):
    print("-----PROBLEM-----")
    print("problem.molecule")
    print(problem.molecule)
    print("problem.basis")
    print(problem.basis)
    print("problem.reference_energy")
    print(problem.reference_energy)
    print("problem.num_particles:")
    print(problem.num_particles)
    print("problem.num_spatial_orbitals")
    print(problem.num_spatial_orbitals)
    print("problem.basis:")
    print(problem.basis)
    print("problem.orbital_energies:")
    print(problem.orbital_energies)
    print("problem.orbital_energies_b:")
    print(problem.orbital_energies_b)
    print("problem.num_alpha:")
    print(problem.num_alpha)
    print("problem.num_beta:")
    print(problem.num_beta)
    print("problem.nuclear_repulsion_energy:")
    print(problem.nuclear_repulsion_energy)
    print("problem.orbital_occupations:")
    print(problem.orbital_occupations)
    print("problem.orbital_occupations_b:")
    print(problem.orbital_occupations_b)
    print("problem.second_q_ops():")
    print(problem.second_q_ops())

    print("-----")
    print("list(problem.second_q_ops()[1].items())[0]:")
    print(list(problem.second_q_ops()[1].items())[0])
    print("-----")
    print("list(problem.second_q_ops()[1].items())[1]:")
    print(list(problem.second_q_ops()[1].items())[1])
    print("-----")
    print("list(problem.second_q_ops()[1].items())[2]:")
    print(list(problem.second_q_ops()[1].items())[2])
    print("-----")
    print("list(problem.second_q_ops()[1].items())[3]:")
    print(list(problem.second_q_ops()[1].items())[3])
    print("-----")
    print("list(problem.second_q_ops()[1].items())[4]:")
    print(list(problem.second_q_ops()[1].items())[4])
    print("-----")
    print("list(problem.second_q_ops()[1].items())[5]:")
    print(list(problem.second_q_ops()[1].items())[5])

#    print("problem.second_q_ops()[0]:")
#    print(problem.second_q_ops()[0])
#    print("problem.second_q_ops()[0].keys():")
#    print(problem.second_q_ops()[0].keys())

#    print("list(problem.second_q_ops()[0].keys())[0]:")
#    print(list(problem.second_q_ops()[0].keys())[0])
#    print("list(problem.second_q_ops()[0].items())[0]:")
#    print(list(problem.second_q_ops()[0].items())[0])
#    print("list(problem.second_q_ops()[0].items())[0][0]:")
#    print(list(problem.second_q_ops()[0].items())[0][0])
#    print("list(problem.second_q_ops()[0].items())[0][1]:")
#    print(list(problem.second_q_ops()[0].items())[0][1])
#
#    print("list(problem.second_q_ops()[0].keys())[1]:")
#    print(list(problem.second_q_ops()[0].keys())[1])
#    print("list(problem.second_q_ops()[0].items())[1]:")
#    print(list(problem.second_q_ops()[0].items())[1])
#
#    print("list(problem.second_q_ops()[0].keys())[2]:")
#    print(list(problem.second_q_ops()[0].keys())[2])
#    print("list(problem.second_q_ops()[0].items())[2]:")
#    print(list(problem.second_q_ops()[0].items())[2])
#
#    print("list(problem.second_q_ops()[0].keys())[3]:")
#    print(list(problem.second_q_ops()[0].keys())[3])
#    print("list(problem.second_q_ops()[0].items())[3]:")
#    print(list(problem.second_q_ops()[0].items())[3])
#
#    print("list(problem.second_q_ops()[0].keys())[4]:")
#    print(list(problem.second_q_ops()[0].keys())[4])
#    print("list(problem.second_q_ops()[0].items())[4]:")
#    print(list(problem.second_q_ops()[0].items())[4])
#
#    print("list(problem.second_q_ops()[1].keys()):")
#    print(list(problem.second_q_ops()[1].keys()))
#
#    print("problem.second_q_ops()[0].items():")
#    print(problem.second_q_ops()[0].items())
#    print("problem.properties.particle_number:")
#    print(problem.properties.particle_number)
#    print("problem.properties.angular_momentum:")
#    print(problem.properties.angular_momentum)
#    print("problem.properties.magnetization:")
#    print(problem.properties.magnetization)
#    print("problem.properties.electronic_dipole_moment:")
#    print(problem.properties.electronic_dipole_moment)
    print("----------")

def print_result_details(result):
    print("-----RESULT-----")
    print("num particles:")
    print(result.num_particles)
    print("spin:")
    print(result.spin)
    print("result.computed_energies:")
    print(result.computed_energies)
    print("result.electronic_energies:")
    print(result.electronic_energies)
#    print("result.frozen_extracted_energy:")
#    print(result.frozen_extracted_energy)
    print("result.groundenergy:")
    print(result.groundenergy)
#    print("result.groundstate:")
#    print(result.groundstate)
    print("result.total_energies:")
    print(result.total_energies)
    # this rounded result.total_energies: isnt always available i guess
    # but it is helpful!
#    print("rounded result.total_energies:")
#    print(round(result.total_energies, 2))
    print("formatted:")
    print(result.formatted())
    print(result)
    print("----------")

def print_energy_details(initial_energy, final_energy):
    print("-----ENERGY-----")
    print("initial_energy")
    print(initial_energy)
    print("final_energy")
    print(final_energy)
    print("----------")

def evolution_to_string(evolution_state):
    evolution_str = ""
#    str = hamiltonian_to_string(evolution_state.hamiltonian)
#    str = str + "\n"
    evolution_str = evolution_str + str(evolution_state.problem)
    evolution_str = evolution_str + "\n"
    evolution_str = evolution_str + str(evolution_state.result)
    evolution_str = evolution_str + "\n"
    evolution_str = evolution_str + str(evolution_state.initial_energy)
    evolution_str = evolution_str + "\n"
    evolution_str = evolution_str + str(evolution_state.final_energy)
    return evolution_str

def print_all(hamiltonian, problem, result, initial_energy, final_energy):
    print_hamiltonian_details(hamiltonian)
    print_problem_details(problem)
    print_result_details(result)
    print_energy_details(initial_energy, final_energy)

# TODO
# trying to collect information about initial and final states so that i can tell
# what a state turns into on the other side
# under the changes of different variables too. thinking of writing tests for this
def print_problem_result(problem, result, max_problem_energy, initial_energy, final_energy, initial_spin:int=0):
    print("|||||")
    print("| PROBLEM LABEL | RESULT LABEL | PROBLEM | RESULT |")
    print("| num_particles | num_particles | " + str(problem.num_particles) + " | " + str(result.num_particles) + " |")
    print("| reference_energy | total_energies | " + str(problem.reference_energy) + " | " + str(result.total_energies[0]) + " |")
    print("| list(problem.second_q_ops()[0].items())[0][1] | groundenergy | " + str(max_problem_energy) + " | " + str(result.groundenergy) + " |")
    # how about nuclear repulsion energy?
    print("| nuclear_repulsion_energy | nuclear_repulsion_energy | " + str(problem.nuclear_repulsion_energy) + " | " + str(result.nuclear_repulsion_energy) + " |")
#    print("| orbital_energies | spin | " + str(problem.orbital_energies) + " | " + str(result.spin) + " |")
#    print("| orbital_energies_b | spin | " + str(problem.orbital_energies_b) + " | " + str(result.spin) + " |")
    print("| initial spin | spin | " + str(initial_spin) + " | " + str(result.spin) + " |")
    print("| initial energy | final energy | " + str(initial_energy) + " | " + str(final_energy) + " |")

class EvolutionSummary:
    def __init__(self,
                 initial_state,
                 final_state,
                 initial_atoms,
                 final_atoms,
                 initial_energy,
                 final_energy,
                 initial_spin,
                 final_spin,
                 initial_num_particles,
                 final_num_particles,
                 hamiltonian,
                 problem,
                 result):
        self.initial_state = initial_state
        self.final_state = final_state
        self.initial_atoms = initial_atoms
        self.final_atoms = final_atoms
        self.initial_energy = initial_energy
        self.final_energy = final_energy
        self.initial_spin = initial_spin
        self.final_spin = final_spin
        self.initial_num_particles = initial_num_particles
        self.final_num_particles = final_num_particles
        self.hamiltonian = hamiltonian
        self.problem = problem
        self.result = result

