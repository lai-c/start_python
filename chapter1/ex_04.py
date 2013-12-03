movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Gramham Chapman",
             ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle",
                 "Terry Jones"]]]
for info in movies:
    if isinstance(info, list):
        for item in info:
            if isinstance(item, list):
                for i in item:
                    print i
            else:
                print item
    else:
        print info
