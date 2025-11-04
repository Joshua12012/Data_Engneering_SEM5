import psycopg2,os
from dotenv import load_dotenv
load_dotenv()

def connect():
    return psycopg2.connect(
        host="localhost",
        database="employees",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )

def getemployeeByID(emp_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT (name, department, contact, email) FROM employees_1 WHERE id=%s",(emp_id,))
    res=cur.fetchone()
    conn.close()
    return res

def getemployeeByDept(dept):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT (name, department, contact, email) FROM employees_1 WHERE department=%s",(dept,))
    res=cur.fetchone()
    conn.close()
    return res