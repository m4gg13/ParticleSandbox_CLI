    
# this isn't used. maybe someday
# basically just add escapes to any double quotes within the string
def scrub_initial_state(initial_state):
    # first, remove newlines
    initial_state = initial_state.replace("\n", "")
    scrubbed_initial_state = initial_state.strip()
    # then find the first index of a double quote
    double_quote_index = initial_state.find('"')
    # a -1 means that there aren't any more double quotes in the given string
    while double_quote_index != -1:
        # place an escape character right before the double quote and put the string back together
        start = scrubbed_initial_state[:double_quote_index]
        end = scrubbed_initial_state[double_quote_index:]
        scrubbed_initial_state = start + "\\" + end
        # now we want to find the next double quote so lets look just beyond where we found the previous
        start_next_double_quote_index = double_quote_index + 4
        # don't want to walk off the end of the string though
        if start_next_double_quote_index > len(scrubbed_initial_state):
            break
        # like we said we'll only look at the end of the string
        # and if we find one we'll use it for the next iteration otherwise it'll be -1
        double_quote_index = scrubbed_initial_state.find('"', start_next_double_quote_index)
    return scrubbed_initial_state