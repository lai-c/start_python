import os


print os.getcwd()  # current working directory
os.chdir('../')  # change the directory
print os.getcwd()  # current working directory
os.chdir('chapter3/')
print os.getcwd()  # current working directory
data = open('sketch.txt')
print data.readline()
print data.readline()
data.seek(0)
print "Hi:"
for each_line in data:
    if each_line.find(":") != -1:
        (role, line_spoken) = each_line.split(':', 1)
        print "%s said:%s" % (role, line_spoken)

data.close()
