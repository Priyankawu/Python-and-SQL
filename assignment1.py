
import sqlite3

#create a database
conn = sqlite3.connect('test.db')
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#while open
with conn:
    #get the cursor that executes sqlite3 commands
    cur = conn.cursor()

    #give cursor the sql command to execute
    cur.execute("CREATE TABLE IF NOT EXISTS \
        tbl(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT)")
    conn.commit()
   #go through list and find .txt files. Add them to table
    for i in fileList:
        if i.endswith('txt'):
            print(i)
            cur.execute("INSERT INTO tbl(col_fname) VALUES(?)", (i))
    conn.commit()
    
conn.close()

