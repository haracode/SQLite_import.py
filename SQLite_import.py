import sqlite3

conn = sqlite3.connect('eScientists.db')
cur = conn.cursor()

#create the Scientists table
#cur.execute('DROP TABLE IF EXISTS Scientists ') #Drop if necessary 
cur.execute('CREATE TABLE Scientists (firstName TEXT, lastName TEXT, department TEXT)')

# open text file of records
try:
    inputFile = open('scientistsUptOct.txt','r') # valid text file?
except:
    print ' Input file cannot be opened.'
    exit()
lineNum = 0 #keep track of all line numbers
errorLines = [] #list to hole the error line number   
scien = 0  #variable to keep track of the number of records 

#read a line of text
for line in inputFile:
   lineNum += 1
   info = line.split()
   if line.isspace() == True: # if line is empty, skip the line
       continue
   # flag & track error lines, skip the line
   if len(info) != 3:
       errorLines.append(lineNum)
       continue
   scien += 1
   cur.execute('INSERT INTO Scientists (firstName, lastName, department) VALUES ( ?, ?, ? )', (info[0], info[1], info[2] ) )

   conn.commit()

print 'total valid records = ', scien, '\n'
#print the database sorted by last name
print 'the records sorted: \n'
cur.execute('SELECT * FROM Scientists ORDER BY lastName')   
for row in cur :
   print row

cur.close()

#flagged error lines (not processed)
print '\n flagged error lines (not processed): ', errorLines
