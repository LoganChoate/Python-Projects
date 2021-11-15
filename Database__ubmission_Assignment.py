##this code imports the relevant libraries
import sqlite3

##this piece of code creates a connection to the specified database
## and initializes the databse with starter values
conn = sqlite3.connect("sub_assign.db")

## this piece of code creates the specified database
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName) \
                ")
    conn.commit()
conn.close()

##this piece of code reads through a list and pulls out certain info
fileList = ("infomation.docx", "Hello.txt", "myImage.png", \
            "myMovie.mpg", "world.txt", "data.pdf", "myPhoto.jpg")
foundIt = []

for item in fileList:
    if ".txt" in item:
        foundIt.append(item)


## this code inserts the searched for values into the database
conn = sqlite3.connect("sub_assign.db")

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fileName, col_fileName) VALUES (?, ?)", \
                (foundIt))
    conn.commit()
conn.close()

##this code prints out the .txt files to the console
conn = sqlite3.connect("sub_assign.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileName FROM tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
    print(msg)
