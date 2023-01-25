

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    user="your_user",
    password="your_password",
    database="your_database"
)

# Create a cursor object
cur = conn.cursor()



# Create a new table that consists of columns from table EMPLOYEE and table DEPARTMENT
cur.execute("""
CREATE TABLE sample_output (
    id SERIAL PRIMARY KEY,
    name_department VARCHAR(255),
    sum(id) INTEGER
)
""")

# Insert data from table EMPLOYEE and table DEPARTMENT into the new table
cur.execute('SELECT DEPARTMENT.name, SUM(EMPLOYEE.id) as total_sum FROM DEPARTMENT JOIN DEPARTMENT ON EMPLOYEE.dept_id = DEPARTMENT.id GROUP BY DEPARTMENT.name into sample_output')


# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

