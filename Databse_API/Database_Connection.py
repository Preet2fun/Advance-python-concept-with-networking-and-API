import MySQLdb
import pandas as pd

# Open database connection
db = MySQLdb.connect("192.168.2.20","root","74557","IMAX_SwitchPortal_V2A_01")

# prepare a cursor object using cursor() method
Cursor = db.cursor()

# execute SQL query using execute() method.
#Cursor.execute("select version()")
Cursor.execute("SELECT EgressSIPCauseCode FROM `Switch_CDRRaw` ORDER BY `CDRInsertTime` DESC")

# Fetch a single row using fetchone() method.
rows = Cursor.fetchone()

#for row in rows:
#            print row[0],"  ",row[1],"  ",row[2],"  "
print rows[0]
#print str(rows)[0:1000]

#print "abc..."
'''
df = pd.DataFrame([[ij for ij in i] for i in rows])
df = pd.DataFrame(i for i in rows)
df.rename(columns={0: 'Egress Cause code', 1: 'Ingress Cause Code', 2: 'ISDN Cause code'}, inplace=True);
#df = df.sort(['Egress Cause code'],  ascending=[0]);
print df.head()

#print rows
#print data[55]
'''
# disconnect from server
db.close()