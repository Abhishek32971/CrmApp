import mysql.connector
dataBase=mysql.connector.connect(host ="localhost",
                                 user ="root",
                                 passwd="root")

#prepare a cursor object 
cursorObject=dataBase.cursor()

#create a database
cursorObject.execute("Create Database elderco")
print("all done!")