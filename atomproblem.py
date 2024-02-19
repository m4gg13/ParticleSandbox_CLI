from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_nature.second_q.mappers import JordanWignerMapper

import json

def evolve(state):
    # make atom - looks like this `"H 0 0 0; H 0 0 0.735"`
    atoms = translate_state_to_atoms(state)
    # determine the problem
    driver = PySCFDriver(
        atom=atoms,
        basis="sto3g",
        charge=0.1,
        spin=0,
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
    elif result.total_energies > problem.reference_energy:
        # the energy increased in the evolution, not sure what that would mean actually!
        print("the energy of the system increased in the evolution")
        final_state = state
#    elif result.total_energies < problem.reference_energy:
#        final_state =
    print_all(hamiltonian, problem, result, initial_energy, final_energy)
    max_problem_energy = find_max_energy(problem)
    print_problem_result(problem, result, max_problem_energy)
    final_state = translate_atoms_to_state(final_atoms)
    return final_state

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
    print("max:")
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
    print("problem.second_q_ops()[0]:")
    print(problem.second_q_ops()[0])
    print("problem.second_q_ops()[0].keys():")
    print(problem.second_q_ops()[0].keys())

    print("list(problem.second_q_ops()[0].keys())[0]:")
    print(list(problem.second_q_ops()[0].keys())[0])
    print("list(problem.second_q_ops()[0].items())[0]:")
    print(list(problem.second_q_ops()[0].items())[0])
    print("list(problem.second_q_ops()[0].items())[0][0]:")
    print(list(problem.second_q_ops()[0].items())[0][0])
    print("list(problem.second_q_ops()[0].items())[0][1]:")
    print(list(problem.second_q_ops()[0].items())[0][1])

    print("list(problem.second_q_ops()[0].keys())[1]:")
    print(list(problem.second_q_ops()[0].keys())[1])
    print("list(problem.second_q_ops()[0].items())[1]:")
    print(list(problem.second_q_ops()[0].items())[1])

    print("list(problem.second_q_ops()[0].keys())[2]:")
    print(list(problem.second_q_ops()[0].keys())[2])
    print("list(problem.second_q_ops()[0].items())[2]:")
    print(list(problem.second_q_ops()[0].items())[2])

    print("list(problem.second_q_ops()[0].keys())[3]:")
    print(list(problem.second_q_ops()[0].keys())[3])
    print("list(problem.second_q_ops()[0].items())[3]:")
    print(list(problem.second_q_ops()[0].items())[3])

    print("list(problem.second_q_ops()[0].keys())[4]:")
    print(list(problem.second_q_ops()[0].keys())[4])
    print("list(problem.second_q_ops()[0].items())[4]:")
    print(list(problem.second_q_ops()[0].items())[4])

    print("list(problem.second_q_ops()[1].keys()):")
    print(list(problem.second_q_ops()[1].keys()))

    print("problem.second_q_ops()[0].items():")
    print(problem.second_q_ops()[0].items())
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
#    print("formatted:")
#    print(result.formatted())
    print(result)
    print("----------")

def print_energy_details(initial_energy, final_energy):
    print("-----ENERGY-----")
    print("initial_energy")
    print(initial_energy)
    print("final_energy")
    print(final_energy)
    print("----------")

def print_all(hamiltonian, problem, result, initial_energy, final_energy):
    print_hamiltonian_details(hamiltonian)
    print_problem_details(problem)
    print_result_details(result)
    print_energy_details(initial_energy, final_energy)

# TODO NEXT
# trying to collect information about initial and final states so that i can tell
# what a state turns into on the other side
# under the changes of different variables too. thinking of writing tests for this
def print_problem_result(problem, result, max_problem_energy):
    print("|||||")
    print("| PROBLEM LABEL | RESULT LABEL | PROBLEM | RESULT |")
    print("| num_particles | num_particles | " + str(problem.num_particles) + " | " + str(result.num_particles) + " |")
    print("| reference_energy | total_energies | " + str(problem.reference_energy) + " | " + str(result.total_energies[0]) + " |")
    print("| list(problem.second_q_ops()[0].items())[0][1] | groundenergy | " + str(max_problem_energy) + " | " + str(result.groundenergy) + " |")
    # how about nuclear repulsion energy?
    print("|  |  | " + str(problem.reference_energy) + " | " + str(result.total_energies[0]) + " |")
