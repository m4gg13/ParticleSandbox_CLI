# sets offer O(1) time complexity for searching!
cache = {(1, "default initial", "default final")}

# example entries for testing
cache.add((1, "H+0.0+001.0", "H+5.0+005.0"))
cache.add((1, "HHHH+0.0-2.0", "HA+1.1-1.1"))

def seek_time_and_initial_state_in_cache(time, initial_state_id):
    for entry in cache:
        if entry[0] == time and entry[1] == initial_state_id:
            final_state_id = entry[2]
            return final_state_id

# given a time delta
# we should be able to find all cached values where the initial state
# as the key is that time delta away from the final state which is
# the value
#
# for example
# for a time of 2
# and an initial state of "HHH+0.2+011.3"
# where the initial state after being evolved twice
# (with minor perturbations to the system)
# ends up in a final state of "HHH+4.2+002.1"
#
# we'd first find
# cache[time] = <array of all state pairs with that time evolution>
# then we'd seek
# cache[time][initial_state_id] = <the final state that we're looking for>
def query(time, initial_state_id):
    final_state_id = seek_time_and_initial_state_in_cache(time, initial_state_id)
    if final_state_id is not None:
        return final_state_id
    else:
        print("failed to find time " + str(time) + " and initial state " + initial_state_id + " in cache")
        # evolve here

def add_entry(entry):
    cache.add(entry)

# MARK: main section
#print(cache)
print(query(1, "H+0.0+001.0"))
