def print_lol(tmp_list, depth):
    for item in tmp_list:
        if isinstance(item, list):
            print_lol(item, depth + 1)
        else:
            print "\t" * depth + "%s" % item

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Gramham Chapman",
             ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
                 "Terry Jones"]]]


print_lol(movies, 1)
