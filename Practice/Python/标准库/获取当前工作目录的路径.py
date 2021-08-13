import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))



# https://stackoverflow.com/questions/22282760/filenotfounderror-errno-2-no-such-file-or-directory
