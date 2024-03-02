import matter
import atom

import atomproblem

def test_evolve():
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0
    hydrogen2.coordinates.z = 0.75
    state = [hydrogen1, hydrogen2]
#    charge = 0
#    spin = 0
    final_state_json = atomproblem.evolve(state)
#    final_state_json = atomproblem.evolve(state, charge, spin)
    print(final_state_json)

def test_evolve_charge():
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0
    hydrogen2.coordinates.z = 0.75
    state = [hydrogen1, hydrogen2]
    basis = "sto3g"
    charge = 2
    spin = 0
    print_all = False
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all)
    print(final_state_json)

def test_evolve_compare_charge():
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0
    hydrogen2.coordinates.z = 0.75
    state = [hydrogen1, hydrogen2]
    basis = "sto3g"
    print_all = False
    print_comparison = True
    print()
    print("***************************")
    print("charge = 2:")
    charge = 2.0
    print("spin = 0:")
    spin = 0
    final_state0_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("charge = 1:")
    charge = 1.0
    print("spin = 1:")
    spin = 1
    final_state1_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("charge = 0:")
    charge = 0
    print("spin = 0:")
    spin = 0
    final_state2_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("charge = -1:")
    charge = -1
    print("spin = 1:")
    spin = 1
    final_state3_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("charge = -2:")
    charge = -2
    print("spin = 0:")
    spin = 0
    final_state4_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()

def test_evolve_compare_coordinates():
    basis = "sto3g"
    charge = 0
    spin = 0
    print_all = False
    print_comparison = True
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (0, 0, 0.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0
    hydrogen2.coordinates.z = 0.75
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (0, 0.75, 0.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0.75
    hydrogen2.coordinates.z = 0.75
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (2, 2, 2)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 2
    hydrogen2.coordinates.y = 2
    hydrogen2.coordinates.z = 2
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (3, 3, 3)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 3
    hydrogen2.coordinates.y = 3
    hydrogen2.coordinates.z = 3
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 4), 2: (4, 4, 4)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 4
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 4
    hydrogen2.coordinates.y = 4
    hydrogen2.coordinates.z = 4
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 5, 5), 2: (5, 5, 5)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 5
    hydrogen1.coordinates.z = 5
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 5
    hydrogen2.coordinates.y = 5
    hydrogen2.coordinates.z = 5
    state = [hydrogen1, hydrogen2]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()

def test_evolve_compare_coordinates_3():
    basis = "sto3g"
    charge = 0
    spin = 1
    print_all = False
    print_comparison = True
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (0, 0, 0.75), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0
    hydrogen2.coordinates.z = 0.75
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (0, 0.75, 0.75), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 0
    hydrogen2.coordinates.y = 0.75
    hydrogen2.coordinates.z = 0.75
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (2, 2, 2), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 2
    hydrogen2.coordinates.y = 2
    hydrogen2.coordinates.z = 2
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 0), 2: (3, 3, 3), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 0
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 3
    hydrogen2.coordinates.y = 3
    hydrogen2.coordinates.z = 3
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 0, 4), 2: (4, 4, 4), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 0
    hydrogen1.coordinates.z = 4
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 4
    hydrogen2.coordinates.y = 4
    hydrogen2.coordinates.z = 4
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()
    print("***************************")
    print("1: (0, 5, 5), 2: (5, 5, 5), 3: (0, 0, 1.75)")
    hydrogen1 = atom.Hydrogen(1)
    hydrogen1.coordinates.x = 0
    hydrogen1.coordinates.y = 5
    hydrogen1.coordinates.z = 5
    hydrogen2 = atom.Hydrogen(1)
    hydrogen2.coordinates.x = 5
    hydrogen2.coordinates.y = 5
    hydrogen2.coordinates.z = 5
    hydrogen3 = atom.Hydrogen(1)
    hydrogen3.coordinates.x = 0
    hydrogen3.coordinates.y = 0
    hydrogen3.coordinates.z = 1.75
    state = [hydrogen1, hydrogen2, hydrogen3]
    final_state_json = atomproblem.evolve(state, basis, charge, spin, print_all, print_comparison)
    print("***************************")
    print()

# MARK: main

#test_evolve()
#test_evolve_charge()
#test_evolve_compare_charge()
#test_evolve_compare_coordinates()
test_evolve_compare_coordinates_3()
