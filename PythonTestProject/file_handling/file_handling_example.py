# Read existing file.
import os

f = open("/Users/hidayath/TestFiles/demofile.txt", "r")
print(f.read())
f.close()

# Read only few characters
f = open("/Users/hidayath/TestFiles/demofile.txt", "r")
print(f.read(5))
f.close()

# Read one line of the file
f = open("/Users/hidayath/TestFiles/demofile.txt", "r")
print(f.readline())
f.close()

# Loop through the file line by line
f = open("/Users/hidayath/TestFiles/demofile.txt", "r")
for x in f:
    print(x)
f.close()

# Open the file "demofile.txt" and append content to the file:
f = open("/Users/hidayath/TestFiles/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("/Users/hidayath/TestFiles/demofile2.txt", "r")
print(f.read())

# Open the file "demofile3.txt" and overwrite the content:
f = open("/Users/hidayath/TestFiles/demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("/Users/hidayath/TestFiles/demofile2.txt", "r")
print(f.read())

# default location is with project directory
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
f.close()

f = open("myfile.txt", "x")
f.write("My file contents")
f.close()

f = open("myfile.txt")
print(f.read())
f.close()

# Delete file
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
