import psycopg2

# connect to the database with credentials
conn = psycopg2.connect("dbname=p1 user=robbie password=wangdong host =127.0.0.1")
# get a cursor to submit queries
cur = conn.cursor()
# #run a selction
cur.execute("select * from resource;")
# #iterate over tuples
for row in cur:
    print(row)
