"""
1a. read - reads the entire contents of the file
2a. read(no of bytes)  - reads the no of bytes that is mentioned

1b. readline - reads one line at a time (1 paragraph)
2b. readline(bytes) - can read within the size of the file

1c. readlines - reads all the lines from the file and stores it in a list
2c. readlines(bytes) - which ever line the byte falls in the entire line will be printed

"""
FL = open("data.txt", "r")

# st = FL.read(10)
st = FL.readlines(857)
print(st)


FL.close()