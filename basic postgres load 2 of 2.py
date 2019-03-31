#the following is for copying data from a csv online into a postgres sql database. while deleting data already there. 
#basic postgres script 2 of 2


#step 1 import libraries and set up connections

import psycopg2
import requests
import csv
import os

conn = psycopg2.connect(.......)
cur = conn.cursor

#step 2 remove existing data from table for new data
cur.execute("DELETE FROM users")

#step 3. use requests to obtain a csv from a url and copy that data from a table (in this case users)

#url = something.com

onlinedata = requests.get(url)
onlinedata.raise_for_status()

with open(onlinedata, 'r') as f:
    next(f)
    cur.copy_from(f,'users',sep=',')

conn.commit()
