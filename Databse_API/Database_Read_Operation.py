import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","pratik","pratik_test")

# prepare a cursor object using cursor() method
Cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "select * from employee where INCOME > '%d'" %(1000)

try :
    # Execute the SQL command
    Cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    result = Cursor.fetchall()
    # Now print fetched result
    for row in result:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s"%(fname,lname,age,sex,income))
except:
    print "Error: unable to fecth data"

# disconnect from server
db.close()