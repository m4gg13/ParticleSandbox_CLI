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
    
    
