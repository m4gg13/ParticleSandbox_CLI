# im sure there are things to import here

def evolve_particle_problem(matter):
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
    final_state = translate_particles_to_final_state(final_particles)
    return final_state
