import mysql.connector

# cursor.execute("CREATE TABLE Job (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, title varchar(50) NOT NULL, company varchar(50) NOT NULL, type varchar(50) NOT NULL, description varchar(4000))")

def insert_job_card(job):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="************",
        database="testdatabase"
    )

    cursor = db.cursor()

    cursor.execute("INSERT INTO Job (title, company, type, description) VALUES (%s, %s, %s, %s)", (job.title, job.company, job.type, job.description))
    db.commit()
