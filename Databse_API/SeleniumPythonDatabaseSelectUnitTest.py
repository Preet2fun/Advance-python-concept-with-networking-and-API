import unittest
import MySQLdb

class PythonDatabaseTests(unittest.TestCase):
    def setUp(self):
        # Open database connection
        self.db = MySQLdb.connect("192.168.2.20","root","74557","IMAX_AdminPortal_V1H_01")

    def test_verify_record_exist(self):
        conn = self.db
        #create a cursor
        cursor = conn.cursor()
        #get all records from the table
        cursor.execute('SELECT * FROM Common_User')
        #fetch all records as dictionary
        records=cursor.fetchall()
        #close the cursor
        cursor.close()
        #print all records
        print records

        for row in records:
            #print record
            User_ID = row[0]
            User_Name = row[1]
            Private_Key = row[2]
            Public_Key = row[3]
            Log_ID = row[4]
            # Now print fetched result
            print "User_ID=%s,User_Name=%s,Private_Key=%s,Public_Key=%s,Log_ID=%s" %(User_ID, User_Name, Private_Key, Public_Key, Log_ID)


        print "total records=%d" % len(records)

    def tearDown(self):
        self.db.close()

if __name__ == "__main__":
    unittest.main()