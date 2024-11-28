from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_nature.second_q.mappers import JordanWignerMapper

import json

import atom
import matter

def run_driver(state, basis:str="sto3g", charge:int=0, spin:int=0):
    # make atom - looks like this `"H 0 0 0; H 0 0 0.735"`
    # atoms = translate_state_to_atoms(state)
    # ugh translate_state_to_atoms isnt putting out properly formatted output i think
    # atoms = "H 0.0 0.0 0.0; H 0.0 0.0 0.735"
    # atoms = "H 0.0 0.0 0.0; H 0.0 0.0 0.735; H 0.0 1.0 2.0; H 0.0 1.0 2.0"
    # atoms = "H 0.0 0.0 0.0; H 0.0 0.0 0.735; H 0.0 0.0 0.745"
    atoms = translate_state_to_atoms(state)
    print_all = True
    print_comparison = True
    final_stateobj = AtomProblemState("initial", state, atoms, basis, charge, spin, print_all, print_comparison)
    # final_stateobj = AtomProblemState("initial", state, atoms, basis, charge, spin, print_all, print_comparison)
    # final_stateobj = AtomProblemState("initial", state, atoms, basis, charge, spin)
    # determine the problem
    if print_all:
        print("** state " + str(state))
        print("** atoms " + str(atoms))
        print("** basis " + str(basis))
        print("** charge " + str(charge))
        print("** spin " + str(spin))
    driver = PySCFDriver(
        atom=atoms,
        basis=basis,
        charge=charge,
        spin=spin,
        unit=DistanceUnit.ANGSTROM,
    )
    problem = driver.run()
    return problem

def evolve_ret_problem(state, basis:str="sto3g", charge:int=0, spin:int=0, do_print_all:bool=False, do_print_comparison:bool=False):
    problem = run_driver(state, basis, charge, spin)
    hamiltonian = problem.hamiltonian
    if do_print_all:
        print_hamiltonian_details(hamiltonian)
        print_problem_details(problem)
    solver = GroundStateEigensolver(
        JordanWignerMapper(),
        NumPyMinimumEigensolver(),
    )
    print('execute computation on quantum computer')
    result = solver.solve(problem)
    if do_print_all:
        print_result_details(result)
    return (problem, result)

# TODO
#  find a way to determine and report what the final state
#   of the system is in terms of type like `matter`, `particle`, `atom`, `molecule`
#   since for ex H_2 atomic input state ends up being a molecule output state
def evolve(state, basis:str="sto3g", charge:int=0, spin:int=0, do_print_all:bool=False, do_print_comparison:bool=False):
    (problem, result) = evolve_ret_problem(state, basis, charge, spin, do_print_all, do_print_comparison)
    return result

def parse_result(initial_state, problem, result, initial_spin:int=0, do_print_all:bool=False, do_print_comparison:bool=False):
    initial_energy = result.initial_energy
    final_energy = result.final_energy
    final_atoms = result.final_atoms
    if initial_energy == final_energy:
        print("the system is the same as it was at the beginning")
        # the initial state can then be returned as the final state
        final_atoms = initial_state
    elif initial_energy > final_energy:
        print("the energy of the system increased in the evolution")
        # TODO - what happens now?
    elif initial_energy < final_energy:
       print("the energy of the system decreased in the evolution")
       # TODO - what happens now?
    if do_print_all:
        print_all(problem.hamiltonian, problem, result, initial_energy, final_energy)
    max_problem_energy = find_max_energy(problem)
    if do_print_comparison:
        print_problem_result(problem, result, max_problem_energy, initial_energy, final_energy, initial_spin)
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

def get_json_evolution_result(initial_state,
                              basis:str="sto3g",
                              charge:int=0, spin:int=0,
                              print_all:bool=False,
                              print_comparison:bool=False):
    evolve_result = evolve(initial_state, basis, charge, spin, print_all, print_comparison)
    # TODO - not sure of a way so far to make `result` into `final_state` or `final_atoms`
    final_state = initial_state
    final_atoms = translate_state_to_atoms(initial_state)
    print('===== final_atoms =====')
    print(final_atoms)
    print('============')
    final_stateobj = AtomProblemState("final",
                                      final_state,
                                      final_atoms,
                                      basis,
                                      charge,
                                      spin,
                                      print_all,
                                      print_comparison)
    return "{\"hydrogen\": 2}"

def get_json_evolution_result_atom_editor(initial_state,charge:int=0, spin:int=0):
    basis = "sto3g"
    print_all = True
    print_comparison = True
    (evolve_problem, evolve_result) = evolve_ret_problem(initial_state, basis, charge, spin, print_all, print_comparison)
    # TODO - not sure of a way so far to make `result` into `final_state` or `final_atoms`
    # final_state = initial_state
    final_atoms = translate_state_to_atoms(initial_state)
    print('===== final_atoms =====')
    print(final_atoms)
    print('============')
    final_state = translate_atoms_to_state(initial_state)
    print('===== final_state =====')
    print(final_state)
    print('============')
    final_stateobj = AtomProblemState("final",
                                      final_state,
                                      final_atoms,
                                      basis,
                                      charge,
                                      spin,
                                      print_all,
                                      print_comparison)
    return (evolve_problem, final_state)


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
                # print("** atom.coordinates " + str(vars(atom.coordinates)))
                # print("** atom.coordinates.x " + str(atom.coordinates.x))
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
    i = 0
    max = 0.0
    while i < 36:
        if abs(list(problem.second_q_ops()[0].items())[i][1]) > abs(max):
            max = list(problem.second_q_ops()[0].items())[i][1]
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
#    print("problem.second_q_ops()[0].items():")
#    print(problem.second_q_ops()[0].items())
    print("problem.properties.particle_number:")
    print(vars(problem.properties.particle_number))
    print("problem.properties.angular_momentum:")
    print(vars(problem.properties.angular_momentum))
    print("problem.properties.magnetization:")
    print(vars(problem.properties.magnetization))
    print("problem.properties.electronic_dipole_moment:")
    print(vars(problem.properties.electronic_dipole_moment))
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
    # this rounded result.total_energies: isnt always available
#    print("rounded result.total_energies:")
#    print(round(result.total_energies, 2))
    print("formatted:")
    print(result.formatted())
    print(result)
    print("----------")

# {'eigenvalues': array([-1.85727503]), 
# 'eigenstates': [(<qiskit.circuit.quantumcircuit.QuantumCircuit object at 0x17ab89310>, None)], 
# 'aux_operators_evaluated': [
# {'AngularMomentum': 0.0, 
# 'Magnetization': 0.0, 
# 'ParticleNumber': (1.999999999999999-4.367323741608634e-17j), 
# 'XDipole': 0.0, 
# 'YDipole': 0.0, 
# 'ZDipole': (1.38894870155532+7.882858934352203e-18j)}
# ], 
# 'raw_result': <qiskit_algorithms.minimum_eigensolvers.numpy_minimum_eigensolver.NumPyMinimumEigensolverResult object at 0x14b64a010>, 
# 'formatting_precision': 12, 
# '_hartree_fock_energy': -1.116998996754004, 
# '_nuclear_repulsion_energy': 0.7199689944489797, 
# '_nuclear_dipole_moment': array([0.       , 0.       , 1.3889487]), 
# '_computed_energies': array([-1.85727503]), 
# '_computed_dipole_moment': [(0.0, 0.0, 1.38894870155532)], 
# '_extracted_transformer_energies': {}, 
# '_extracted_transformer_dipoles': [{}], 
# '_reverse_dipole_sign': True, 
# '_num_particles': [1.999999999999999], 
# '_magnetization': [0.0], 
# '_total_angular_momentum': [0.0], 
# '_electronic_density': None}
def print_evolution_state(evolution_state):
    print("-----RESULT-----")
    print("eigenvalues:")
    print(result.eigenvalues)
    print("eigenstates:")
    print(vars(result.eigenstates))
    print("aux_operators_evaluated:")
    print(aux_operators_evaluated)
    # print("spin:")
    # print(result.spin)
    # print("result.computed_energies:")
    # print(result.computed_energies)
    # print("result.electronic_energies:")
    # print(result.electronic_energies)
#    print("result.frozen_extracted_energy:")
#    print(result.frozen_extracted_energy)
    # print("result.groundenergy:")
    # print(result.groundenergy)
#    print("result.groundstate:")
#    print(result.groundstate)
    # print("result.total_energies:")
    # print(result.total_energies)
    # this rounded result.total_energies: isnt always available
#    print("rounded result.total_energies:")
#    print(round(result.total_energies, 2))
    print("formatted:")
    print(result.formatted())
    # print(result)
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

