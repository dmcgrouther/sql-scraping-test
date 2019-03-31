#the following is for creating a table in postgressql and copying data from a csv online to this database
#basic postgres script 1 of 2

#step 1 import libraries and set up connections

import psycopg2
import requests
import csv
import os

conn = psycopg2.connect(.......)
cur = conn.cursor

#step 2 create table in database

cur.execute("""
    CREATE TABLE users(
    id integer PRIMARY KEY,
    email text,
    name text,
    address text)
""")

#step 3. use requests to obtain a csv from a url and copy that data from a table (in this case users)

#url = something.com

onlinedata = requests.get(url)
onlinedata.raise_for_status()

with open(onlinedata, 'r') as f:
    next(f)
    cur.copy_from(f,'users',sep=',')

conn.commit()
