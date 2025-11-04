from flask import Flask
import psycopg2,os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/')
def connect():
    return psycopg2.connect(
        host="localhost",
        database="employees",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route('/<int:emp_id>')
def getemployeeByID(emp_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT (name, department, contact, email) FROM employees_1 WHERE id=%s",(emp_id,))
    res=cur.fetchone()
    if not res:
        print("None")
    conn.close()
    return f"Employee details : {res}"

@app.route('/<dept>')
def getemployeeByDept(dept):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT (name, department, contact, email) FROM employees_1 WHERE department=%s",(dept,))
    res=cur.fetchall()
    if not res:
        print("None")
    conn.close()
    return f"Employee details : {res}"