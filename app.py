from flask import *
app = Flask("__name__")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/Search', methods = ["POST"])

def Search():
    data = request.form
    sch = data["sch"]
    dept = data["dept"]

    import sqlite3
    conn = sqlite3.connect("schools.db")

    COMMAND = """
    SELECT sch.Name, s.Name, s.Department, s.Contact, sch.Address
    FROM SCHOOL sch, STAFF s
    WHERE sch.SchoolCode = s.SchoolCode AND sch.Name like ? AND s.Department = ?
    """

    cursor = conn.execute(COMMAND,("%" + sch + "%", dept)).fetchall()
    conn.close()

    return render_template("results.html",
        cursor = cursor)
    
if __name__ == "__main__":
    app.run(port = 1001, debug = True)
