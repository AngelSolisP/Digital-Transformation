my_file = open("my_file.txt", "w")
my_file.write("Hello, World!\n")
my_file.write("This is a test file.\n")
my_file.close()

my_file = open("my_file.txt", "r")
content = my_file.read()
print(content)