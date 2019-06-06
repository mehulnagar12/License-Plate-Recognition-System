import sqlite3 
connection = sqlite3.connect("Table.db") 

# cursor 
crsr = connection.cursor() 

# SQL command to create a table in the database
sql_command = """create table new(
ID int,
Name varchar(50),
Phone_Number integer(10),                               
Address VARCHAR(250), 
Account_Number integer(15),
Account_Balance int);"""
crsr.execute(sql_command) 

sql_command = """create table tax(
Name_Vehicle varchar(50),
Challan_Amount int);"""
# execute the statement 
crsr.execute(sql_command) 

# SQL command to insert the data in the table 
sql_command = """INSERT INTO new VALUES (1, "Rishabh", "8494959495", "M", "2014264","5623");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO new VALUES (2, "Bill", "1234667809", "M", "19801028","123");"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO tax VALUES("Bike",70)"""
crsr.execute(sql_command)

sql_command = """INSERT INTO tax VALUES("Maruti",100)"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO tax VALUES("SUV",500)"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO tax VALUES("Bus",700)"""
crsr.execute(sql_command) 

sql_command = """INSERT INTO tax VALUES("Truck",1000)"""
crsr.execute(sql_command) 

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database. 
connection.commit() 

#fatch all data
crsr.execute("select * from new")
data = crsr.fetchall()
for i in data:
    print(i);
print(" ")

crsr.execute("select * from tax")
data = crsr.fetchall()
for j in data:
    print(j);

print(" ")


a = int(input("Enter the ID: "))
b = int(input("Enter the amount to be deducted: "))


connection.execute("update new set Account_Balance = Account_Balance - 200  where ID = " + str(a))
connection.commit()

print ("Total number of rows updated: ",connection.total_changes)


#fatch all data
crsr.execute("select * from new")
da = crsr.fetchall()

for k in da:
    print(k);
# close the connection 
connection.close()
