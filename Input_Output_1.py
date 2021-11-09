##This is the import for the file input and output library
import os

##this code uoipens a file, reads through it and prints out the text content
with open('IO_test_1.txt', 'r') as f:
    data = f.read();
    print(data);
    f.close();

def writeData():
    data = "\n Hello World!";
    with open("IO_test_1.txt", "a") as f1:
        f1.write(data);
        f1.close();

def openFile():
    with open("IO_test_1.txt", "r") as f1:
        data = f1.read();
        print(data);
        f1.close();
        
if __name__ == "__main__":
    writeData()
    openFile()

##############################################################################

##This code is more examples of File IO
import os

fName = "Hello"

fPath = "c:\\A\\"

abPath = os.path.join(fPath, fName)
print(abPath)
