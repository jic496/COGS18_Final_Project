"""Script to run some part of my project."""

# # This adds the directory above to our Python path
# #   This is so that we can add import our custom python module code into this script
# import sys
# sys.path.append('../')

# # Imports
# from my_module.functions import my_func, my_other_func

# ###
# ###

# # PYTHON SCRIPT HERE

# pass

from my_module.functions import File, FileSystem
from my_module.test_functions import test_ls, test_read_content

# Test functions
test_ls()
test_read_content()

file_system = FileSystem()

# list all files and directories under current director: should return an empty list
print ('The list of directories and file under current directory is: ' + str(file_system.ls("/")))

# make new directories: d1 and d2 under current director
print ("Make two new directories: d1 and d2 under current director")
file_system.mkdir("/d1")
file_system.mkdir("/d2")
print ("The list of directories and file under current directory is:" + str(file_system.ls("/")))

# create new directories d1_1, d1_2 and d1_3 under d1
print ("Make three new directories d1_1, d1_2 and d1_3 under d1")
file_system.mkdir("/d1/d1_1")
file_system.mkdir("/d1/d1_2")
file_system.mkdir("/d1/d1_3")
print ("The list of directories and file under d1 is:" + str(file_system.ls("/d1")))

# create a new file f1 under d1_2
print ("Make a new file f1 under d1_2")
file_system.mkdir("/d1/d1_2/f1")

# create a new file f3 under directory /d1/d1_1/d1_1_1 where d1_1_1 is the middle director which does not exist
file_system.mkdir("/d1/d1_1/d1_1_1/f3")
print ("The list of directories and file under d1_1 is:" + str(file_system.ls("/d1/d1_1")))
print ("The list of directories and file under d1_1_1 is:" + str(file_system.ls("/d1/d1_1/d1_1_1")))

# add a text content "This is a new content!" to a file which already exists f1
print ("Add new content to f1")
file_system.addContentToFile("/d1/d1_2/f1", "This is a new content!")

# read the content from f1
print ("Read content from file f1")
print ("The content read from f1 is: " + file_system.readContentFromFile("/d1/d1_2/f1"))

print ("Add another new content to f1")
file_system.addContentToFile("/d1/d1_2/f1", "This is another new content!")

# read the content from f1
print ("Read content from file f1")
print ("The content read from f1 is: " + file_system.readContentFromFile("/d1/d1_2/f1"))

# add new content to a file which does not exist, e.g.: f3 under d1_2
print ("Add content to a new file")
file_system.addContentToFile("/d1/d1_2/f3", "This is a new content add to a file which does not exist!")
# read the content from f2
print ("The content read from f3 is: " + file_system.readContentFromFile("/d1/d1_2/f3"))