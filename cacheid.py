import atom

def get_atoms_from_id(id):
    # at first the id is like this 'HHHH+0.0-2.0'
    particles = id.split('+', 1)
    # now the id is like this ['HHHH', '0.0-2.0']
    atoms = []
    if len(particles) > 0:
        for char in particles[0]:
            match char:
                case "H":
                    atoms.append(atom.Hydrogen(3))
    return atoms

def get_num_particles_from_id(id):
    particles = id.split('+', 1)
    count = 0
    if len(particles) > 0:
        for char in particles[0]:
            count += 1
    return count

def get_spin_from_id(id):
    # at first the id is like this 'HHHH+0.0-2.0'
    spin = id.split('+', 1)
    # now the id is like this ['HHHH', '0.0-2.0']
    if len(spin) > 1:
        if '+' in spin[1]:
            return spin[1].split('+', 1)[0]
        else:
            return spin[1].split('-', 1)[0]

def get_energy_from_id(id):
    # at first the id is like this 'HHHH+0.0-2.0'
    energy = id.split('+', 1)
    # now the id is like this ['HHHH', '0.0-2.0']
    print("energy")
    print(energy)
    if len(energy) > 1:
        if'+' in energy[1]:
            return energy[1].split('+', 1)[1]
        else:
            return "-" + energy[1].split('-', 1)[1]

# testing
def test_get_num_particles_from_id():
    print("get_num_particles_from_id('HHHH+0.0-2.0')")
    a = get_num_particles_from_id("HHHH+0.0-2.0")
    print(str(a))
    print("4 == " + str(a) + ": " + str(4 == a))

def test_get_spin_from_id():
    print("get_spin_from_id('HHHH+0.0-2.0')")
    a = get_spin_from_id("HHHH+0.0-2.0")
    print(str(a))
    print("0.0 == " + str(a) + ": " + str("0.0" == a))

def test_get_energy_from_id():
    print("get_energy_from_id('HHHH+0.0-2.0')")
    a = get_energy_from_id("HHHH+0.0-2.0")
    print(str(a))
    print("-2.0 == " + str(a) + ": " + str("-2.0" == a))

def test_get_atoms_from_id():
    print("get_atoms_from_id('HHHH+0.0-2.0')")
    a = get_atoms_from_id("HHHH+0.0-2.0")
    print(str(a))
    h1 = atom.Hydrogen(4)
    h2 = atom.Hydrogen(5)
    h3 = atom.Hydrogen(6)
    h4 = atom.Hydrogen(7)
    e = [h1, h2, h3, h4]
    print(str(a) + " == " + str(e) + " : " + str((str(a) == str(e))))

# main

#test_get_num_particles_from_id()
#test_get_spin_from_id()
#test_get_energy_from_id()
test_get_atoms_from_id()
