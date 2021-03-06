"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open('src/foo.txt', 'r')
print(f.read())
f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

f2 = open('src/bar.txt', 'w')
f2.write("You think darkness is your ally?\n I was born in it, \n raise by it. It wasn't until I was a man when I saw the light and it was blinding!")
f2.close()
