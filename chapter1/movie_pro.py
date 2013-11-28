movies = ["The Holy Grail",
          "The Life of Brian",
          "The Meaning of Life"]
print movies
print movies[1]
print "hello, %s" % movies[1]
print "movies' lenght :%d" % len(movies)
movies.append("The Brian Gilliam")
print movies
print "after append movies' lenght :%d" % len(movies)
tailEle = movies.pop()
print tailEle
print movies
print "after pop movies' lenght :%d" % len(movies)
another_movie_list = ["Gilliam", "Chapman"]
movies.extend(another_movie_list)
print movies
