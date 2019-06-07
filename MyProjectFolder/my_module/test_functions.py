"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import File, FileSystem

file_system = FileSystem()
file_system.mkdir("/")
file_system.mkdir("/d1/d2/f1")
file_system.addContentToFile("/d1/d2/f1","add a new content to this file")

def test_ls():
    assert file_system.ls("/") == ['', 'd1']
    assert file_system.ls("/d1") == ['d2']
    assert file_system.ls("/d1/d2") == ['f1']

def test_read_content():
    assert file_system.readContentFromFile("/d1/d2/f1") == "add a new content to this file"
