try:
    file = open("./Assets/Test.txt","r");
    file.write("errr")
except IOError:
    print("error")
else:
    print ("no error")