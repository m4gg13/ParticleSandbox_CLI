from qiskit_nature.units import DistanceUnit
from qiskit_nature.second_q.drivers import PySCFDriver

from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_nature.second_q.algorithms import GroundStateEigensolver
from qiskit_nature.second_q.mappers import JordanWignerMapper

def evolve(state):
    print("state:")
    print(state[0].name)
    # make atom - looks like this `"H 0 0 0; H 0 0 0.735"`
    atom = "H 0 0 0; H 0 0 0.735"
    # determine the problem
    driver = PySCFDriver(
        atom=atom,
        basis="sto3g",
        charge=0,
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
    final_state = []
    print_energy_details(initial_energy, final_energy)
    if initial_energy == final_energy:
        # then the system is the same as it was at the beginning
        # and we can return the initial state as the final state
        print("state 1:")
        print(state[0].name)
        final_state = state
#    elif result.total_energies > problem.reference_energy:
        # the energy increased in the evolution, not sure what that would mean actually!
#        final_state = state
#    elif result.total_energies < problem.reference_energy:
#        final_state =
#    print_all(hamiltonian, problem, result, initial_energy, final_energy)
    final_atoms = translate_state_to_atoms(final_state)
    return final_atoms

def translate_state_to_atoms(state):
    i = 0
    final_atoms = ""
    for atom in state:
        # if this isn't the first atom, add a semicolon
        if i > 0:
            final_atoms += "; "
        # figure out what kind of atom we're dealing with
        print("atom.name:")
        print(atom.name)
        match atom.name:
            case "hydrogen":
                # make atom - looks like this for example `"H 0 0 0; H 0 0 0.735"`
                coordinates = atom.coordinates.describe()
                final_atoms = final_atoms + "H " + coordinates
        i+=1
    print("final_atoms:")
    print(final_atoms)
    return final_atoms

# MARK: logging

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
    print("problem.reference_energy")
    print(problem.reference_energy)
    print("problem.num_particles:")
    print(problem.num_particles)
    print("problem.num_spatial_orbitals")
    print(problem.num_spatial_orbitals)
    print("problem.basis:")
    print(problem.basis)
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
    print("rounded result.total_energies:")
    print(round(result.total_energies, 2))
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
