#persistant data files are files that are saved to the hard disk and can be retrieved later. Python has built in functions to help us with data saving and retrieval

#there are many types of files we can work with - csv, text, certain excel/spreadsheets, etc...
#create and write to a text file
#so to make or open any file we use the open() function to open up a connection the file
#open(filename, argument for reading or writing data)

#writing - make a new file if none exists, and override it if it does (replace), and write data to it.
#nothing to import
#w stands for write
file = open("myfile.txt", "w")
#call the .write() function to write to a file
file.write("File now has some text \n")
file.write("File has another line of text \n")
#when done with a file we always have to close it so it can be opened later or is not left hanging
file.close()

#read from the file by using the 'r' argument
# f = open("myfile.txt", "r")
# #we can read one line at a time with the readline()
# print(f.readline())
# print(f.readline())
# f.close()

#Some utilities built into python to help read multiple lines
#with keyword that means with this file do the following
#the with keyword is very useful because it automatically closes when done processing the file
with open("myfile.txt", "r") as myfile:
    #loop to read lines
    while True:
        line = myfile.readline()
        if not line: #this will check to see if a line is empty (EOF)
            break
        print(line)

#if we want to add to an existing file
# 'a' or append argument

with open("myfile.txt", "a") as myfile:
    myfile.write("This is text I added using append")


#check to see if text was added
with open("myfile.txt", "r") as myfile:
    #loop to read lines
    while True:
        line = myfile.readline()
        if not line: #this will check to see if a line is empty (EOF)
            break
        print(line)