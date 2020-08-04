import psycopg2
connection = psycopg2.connect(database="test-gps", user="rezelput",
password="123")
cursor = connection.cursor()
cursor.execute("SELECT id,name FROM cities WHERE pop>100000")
for row in cursor:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE borders (" +
                   "id SERIAL PRIMARY KEY," +
                   "name VARCHAR NOT NULL," +
                   "iso_code VARCHAR NOT NULL," +
                   "outline GEOGRAPHY)")
    cursor.execute("CREATE INDEX border_index ON borders " +
                   "USING GIST(outline)")
    connection.commit()