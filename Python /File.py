

file = open("./Assets/Test.txt", "a+")

file.write("nagaraj\n")
str=file.read(10);
print(str)
file.close()