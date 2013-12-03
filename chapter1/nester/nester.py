"""This is the "nester.py" module and it provides one function called
   print_lol() which prints lists that may or may not include nested lists."""
def print_lol(tmp_list, depth):
    """This function takes one positional argument called "tmp_list", which is
    any Python list. Each data item in the provided list is (recursively) 
    printed to the screen on it's own line, and another argument callled 
    "depth", which control the indent of the output."""
    for item in tmp_list:
        if isinstance(item, list):
            print_lol(item, depth + 1)
        else:
            print "\t" * depth + "%s" % item
